"""
windows.py -- Links components of the graphical user interface.
Copyright (C) 2021  Paul Sirri <paulsirri@gmail.com>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

# File Description:
# This file contains the logic for linking together the components of the frontend.
# In the UI directory (src/main/python/ui/) custom PyQt5 QMainWindow classes are defined.
# Here, those custom classes are given functionality and linked together.


from PyQt5.QtGui import QImage, QPixmap, QGuiApplication, QFont, QColor, QCursor
from PyQt5.QtCore import Qt, QTime, QDate, QDateTime
from PyQt5.QtWidgets import QMainWindow, QAbstractItemView, QTableWidget, QTableWidgetItem, \
    QDialog, QProgressBar, QFileDialog, QLabel, QGridLayout, QWidget, QDesktopWidget, QLineEdit, \
    qApp

from ui.ui_20210204.StartScreen_v32 import Ui_MainWindow as Start_Ui
# from ui.ui_20201106.FileSelection_v18_dawn import Ui_MainWindow as File_Ui_Standard
from ui.ui_20210204.FileSelection_Standard_v20 import Ui_MainWindow as File_Ui_Standard
# from ui.ui_20200906.FileSelection_v13 import Ui_MainWindow as File_Ui_DetachedLabel
from ui.ui_20210204.FileSelection_Detached_v20 import Ui_MainWindow as File_Ui_DetachedLabel
from ui.ui_20210204.SignalAnalysis_v38 import Ui_MainWindow as Signal_Ui
from ui.ui_20210204.ExportMenu_v2 import Ui_MainWindow as ExportMenu_Ui
from ui.ui_20210129.glucokeep_about import Ui_MainWindow as About_Ui
from ui.ui_20210204.UserdefinedMenu_v2 import Ui_MainWindow as Userdefined_Ui

from read_data import find_polar_pair, file_to_numpy, get_iq_data, get_files, get_sample_rate, \
    strftime_DOY, strftime_hhmmss, strftime_yyyyDOYhhmmss, strftime_yyyyDOYhhmmssff, \
    strftime_yyyyDOY, strftime_timestamp, get_polar_compliment, convert_astropy_to_pyqt, \
    convert_pyqt_to_astropy
from signal_processing import get_signal_processing_parameters
from spectral_analysis import get_spectral_analysis_results
from astropy.time import Time, TimeDelta
import numpy as np
import time
import os

import matplotlib

matplotlib.use('Qt5Agg')
from PyQt5 import QtCore, QtWidgets
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar


class StartWindow(QMainWindow, Start_Ui):
    def __init__(self, ctx, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ctx = ctx
        self.setupUi(self)

        # set the window title
        self.setWindowTitle("PARSE - Start")

        # set text to be selectable
        set_text_selectable(self)

        # set window size
        w = 700
        h = 700
        self.resize(w, h)

        # center the window
        center_window(self)

        # format text
        self.lbl_title.setStyleSheet('font-size: 22px; font: "Arial"')
        self.lbl_version.setStyleSheet('font-size: 12px; font: "Arial"')
        self.lbl_version.setText('Version 1\n2021.02.04')
        self.lbl_open_desc.setStyleSheet('font-size: 14px; font: "Arial"')

        # add the large PARSE graphic to be shown on the start window
        pixmap_parse_logo = QPixmap(QImage(self.ctx.img_parse_logo()))
        pixmap_parse_logo = pixmap_parse_logo.scaled(
            300, 300, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.label_parselogo.setPixmap(pixmap_parse_logo)
        self.label_parselogo.setAlignment(Qt.AlignCenter)

        # add the small USC logo to be shown on the start window
        pixmap_usc_logo = QPixmap(QImage(self.ctx.img_usc_logo()))
        pixmap_usc_logo = pixmap_usc_logo.scaled(
            130, 130, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.label_usclogo.setPixmap(pixmap_usc_logo)
        self.label_usclogo.setAlignment(Qt.AlignRight | Qt.AlignBottom)
        self.label_usclogo.setContentsMargins(0, 0, 12, 8)  # (left, top, right, bottom)

        self.btn_documentation.setText("User's Guide")

        # connect signals and slots
        self.btn_dawnvesta.clicked.connect(self.choose_dawn)
        self.btn_rosetta.clicked.connect(self.choose_rosetta)
        self.btn_userfile.clicked.connect(self.choose_userfile)

        self.btn_tutorial.clicked.connect(self.show_tutorial)
        self.btn_documentation.clicked.connect(self.show_userguide)
        self.btn_sourcecode.clicked.connect(self.show_sourcecode)
        self.btn_about.clicked.connect(self.show_publications)
        self.btn_contact.clicked.connect(self.show_contact)

    def choose_dawn(self):
        self.file_window = FileWindowStandard(self.ctx, source='dawn')
        self.file_window.show()
        self.close()

    def choose_rosetta(self):
        self.file_window = FileWindowDetachedLabel(self.ctx, source='rosetta')
        self.file_window.show()
        self.close()

    def choose_userfile(self):
        self.userdefined_window = UserdefinedWindow(self.ctx, source='userfile')
        self.userdefined_window.show()
        self.close()

    def show_tutorial(self):
        self.tutorial_window = TutorialWindow(self.ctx)
        self.tutorial_window.show()
        self.close()

    def show_userguide(self):
        self.userguide_window = ManualWindow(self.ctx)
        self.userguide_window.show()
        self.close()

    def show_sourcecode(self):
        self.sourcecode_window = SourceCodeWindow(self.ctx)
        self.sourcecode_window.show()
        self.close()

    def show_publications(self):
        self.publications_window = PublicationsWindow(self.ctx)
        self.publications_window.show()
        self.close()

    def show_contact(self):
        self.contact_window = ContactUsWindow(self.ctx)
        self.contact_window.show()
        self.close()


class TutorialWindow(QMainWindow, About_Ui):
    def __init__(self, ctx, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ctx = ctx
        self.setupUi(self)

        # set the title
        self.setWindowTitle("PARSE - Tutorial")

        # set text to be selectable
        set_text_selectable(self)

        # connect UI elements using slots and signals
        self.pushButton.clicked.connect(self.back_to_menu)

        self.label.setText("A video tutorial is available through the Youtube link below:")

        # provide link to email
        self.label_2.setOpenExternalLinks(True)
        self.label_2.setText(
            "<a href=https://www.youtube.com>https://www.youtube.com</a>")
        self.label_2.setTextInteractionFlags(Qt.TextSelectableByMouse | Qt.LinksAccessibleByMouse)

        self.label_3.setText("")

        # center the window
        center_window(self)

    def back_to_menu(self):
        self.start_window = StartWindow(self.ctx)
        self.start_window.show()
        self.close()


class ManualWindow(QMainWindow, About_Ui):
    def __init__(self, ctx, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ctx = ctx
        self.setupUi(self)

        # set the title
        self.setWindowTitle("PARSE - Manual")

        # set text to be selectable
        set_text_selectable(self)

        # connect UI elements using slots and signals
        self.pushButton.clicked.connect(self.back_to_menu)

        self.label.setText(
            "A copy of the official User's Guide is available through the link below:")

        # provide link to email
        self.label_2.setOpenExternalLinks(True)
        self.label_2.setText(
            "<a href=https://github.com/PARSE-team/PARSE/blob/main/Manual.pdf>"
            "https://github.com/PARSE-team/PARSE/blob/main/Manual.pdf</a>")
        self.label_2.setTextInteractionFlags(Qt.TextSelectableByMouse | Qt.LinksAccessibleByMouse)

        self.label_3.setText("")

        # center the window
        center_window(self)

    def back_to_menu(self):
        self.start_window = StartWindow(self.ctx)
        self.start_window.show()
        self.close()


class SourceCodeWindow(QMainWindow, About_Ui):
    def __init__(self, ctx, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ctx = ctx
        self.setupUi(self)

        # set the title
        self.setWindowTitle("PARSE - Source Code")

        # set text to be selectable
        set_text_selectable(self)

        # connect UI elements using slots and signals
        self.pushButton.clicked.connect(self.back_to_menu)

        self.label.setText("To view source code or learn more about PARSE,\n"
                           "please visit the project's official GitHub page:")

        # provide link to GitHub
        self.label_2.setOpenExternalLinks(True)
        self.label_2.setText(
            "<a href=https://github.com/PARSE-team/PARSE>https://github.com/PARSE-team/PARSE</a>")
        self.label_2.setTextInteractionFlags(Qt.TextSelectableByMouse | Qt.LinksAccessibleByMouse)

        self.label_3.setText("")

        # center the window
        center_window(self)

    def back_to_menu(self):
        self.start_window = StartWindow(self.ctx)
        self.start_window.show()
        self.close()


class PublicationsWindow(QMainWindow, About_Ui):
    def __init__(self, ctx, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ctx = ctx
        self.setupUi(self)

        # set the title
        self.setWindowTitle("PARSE - Relevant Publications")

        # set text to be selectable
        set_text_selectable(self)

        # connect UI elements using slots and signals
        self.pushButton.clicked.connect(self.back_to_menu)

        # fill and format the publications
        self.fill_in_publications()

        # set window size
        w = 500
        h = 500
        self.resize(w, h)

        # center the window
        center_window(self)

    def back_to_menu(self):
        self.start_window = StartWindow(self.ctx)
        self.start_window.show()
        self.close()

    def fill_in_publications(self):
        """ A method to fill and format the contents of the publications window. """

        self.verticalLayout.setSpacing(4)
        self.verticalLayout.setContentsMargins(20, 0, 0, 0)  # (left, top, right, bottom)
        self.label_2.setText('')
        self.label_3.setText('')

        self.label.setText("RELEVANT PUBLICATIONS:")
        self.label.setStyleSheet('font-size: 17px; font: "Arial";')

        # PyQt5 v5.9.2 has bug where whitespaces in text strings do not render correctly on MacOS
        # manually replace these whitespace characters with white underscores ("_")
        w = "< font color='White' size=3 ><sub>_</sub></font>"

        recommended_label = QLabel('RECOMMENDED READING')
        recommended_label.setStyleSheet('font-size: 13px; font: "Arial"; font-weight: bold;')
        recommended_label.setTextInteractionFlags(Qt.TextSelectableByMouse)
        self.verticalLayout.insertWidget(4, recommended_label)
        self.verticalLayout.insertWidget(5, QLabel(''))

        pub1_desc = QLabel("Palmer,{}E.{}M.,{}Sirri,{}P.{}& Heggy,{}E.{}(2021).{}A User "
                           "Interface for the Processing and Analysis of Deep Space Network "
                           "Planetary Radio Science Data.{}SoftwareX "
                           "(Elsevier).".format(w, w, w, w, w, w, w, w, w))
        pub1_desc.setTextInteractionFlags(Qt.TextSelectableByMouse)
        pub1_link = QLabel('[Submitted for Review]')
        # pub1_link.setOpenExternalLinks(True)
        pub1_link.setTextInteractionFlags(Qt.TextSelectableByMouse | Qt.LinksAccessibleByMouse)
        pub1_link.setStyleSheet('font-size: 13px; font: "Arial"; padding: 0px 0px 0px 34px;')
        self.verticalLayout.insertWidget(6, pub1_desc)
        self.verticalLayout.insertWidget(7, pub1_link)  # no link (yet!)
        self.verticalLayout.insertWidget(8, QLabel(''))

        pub2_desc = QLabel('Palmer,{}E.{}M.,{}Heggy,{}E.{}& Kofman,{}W.{}(2017).{}Orbital '
                           'bistatic radar observations of asteroid Vesta by the Dawn '
                           'mission.{}Nature Communications,{}8(409),{}1–12.{}[Open '
                           'Access]'.format(w, w, w, w, w, w, w, w, w, w, w, w))
        pub2_desc.setTextInteractionFlags(Qt.TextSelectableByMouse)
        pub2_link = QLabel('<a href=https://doi.org/10.1038/s41467-017-00434-6>'
                           'doi:10.1038/s41467-017-00434-6</a>')
        pub2_link.setOpenExternalLinks(True)
        pub2_link.setTextInteractionFlags(Qt.TextSelectableByMouse | Qt.LinksAccessibleByMouse)
        pub2_link.setStyleSheet('font-size: 13px; font: "Arial"; padding: 0px 0px 0px 34px;')
        self.verticalLayout.insertWidget(9, pub2_desc)
        self.verticalLayout.insertWidget(10, pub2_link)
        self.verticalLayout.insertWidget(11, QLabel(''))

        pub3_desc = QLabel('Palmer,{}E.{}M.{}& Heggy,{}E.{}(2020).{}Bistatic Radar Occultations '
                           'of Planetary Surfaces.{}IEEE Geoscience & Remote Sensing '
                           'Letters,{}17(5),{}804–808.'.format(w, w, w, w, w, w, w, w, w))
        pub3_desc.setTextInteractionFlags(Qt.TextSelectableByMouse)
        pub3_link = QLabel('<a href=https://doi.org/10.1109/LGRS.2019.2931310>'
                           'doi:10.1109/LGRS.2019.2931310</a>')
        pub3_link.setOpenExternalLinks(True)
        pub3_link.setTextInteractionFlags(Qt.TextSelectableByMouse | Qt.LinksAccessibleByMouse)
        pub3_link.setStyleSheet('font-size: 13px; font: "Arial"; padding: 0px 0px 0px 34px;')
        self.verticalLayout.insertWidget(12, pub3_desc)
        self.verticalLayout.insertWidget(13, pub3_link)
        self.verticalLayout.insertWidget(14, QLabel('\n'))

        further_label = QLabel('FURTHER READING')
        further_label.setStyleSheet('font-size: 13px; font: "Arial"; font-weight: bold;')
        further_label.setTextInteractionFlags(Qt.TextSelectableByMouse)
        self.verticalLayout.insertWidget(15, further_label)
        self.verticalLayout.insertWidget(16, QLabel(''))

        pub4_desc = QLabel(
            'Simpson,{}R.{}A.{}(1993).{}Spacecraft studies of planetary surfaces using bistatic '
            'radar.{}IEEE Transactions on Geoscience and Remote '
            'Sensing,{}31(2),{}465–482.'.format(w, w, w, w, w, w, w))
        pub4_desc.setTextInteractionFlags(Qt.TextSelectableByMouse)
        pub4_link = QLabel(
            '<a href=https://doi.org/10.1109/36.214923>doi:10.1109/36.214923</a>')
        pub4_link.setOpenExternalLinks(True)
        pub4_link.setTextInteractionFlags(Qt.TextSelectableByMouse | Qt.LinksAccessibleByMouse)
        pub4_link.setStyleSheet('font-size: 13px; font: "Arial"; padding: 0px 0px 0px 34px;')
        self.verticalLayout.insertWidget(17, pub4_desc)
        self.verticalLayout.insertWidget(18, pub4_link)
        self.verticalLayout.insertWidget(19, QLabel(''))

        pub5_desc_a = QLabel(
            "Simpson,{}R.{}A.,{}Tyler,{}G.{}L.,{}Pätzold,{}M.,{}Häusler,{}B.,{}Asmar,{}S.{}W.{}& "
            "Sultan-Salem,{}A.{}K.{}(2011).{}Polarization in Bistatic Radar "
            "Probing of Planetary".format(w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w))
        pub5_desc_a.setTextInteractionFlags(Qt.TextSelectableByMouse)
        pub5_desc_b = QLabel(
            "Surfaces: Application to Mars Express Data.{}Proceedings "
            "of the IEEE,{}99(5),{}858–874.".format(w, w, w))
        pub5_desc_b.setStyleSheet('font-size: 13px; font: "Arial"; padding: 0px 0px 0px 34px;')
        pub5_desc_b.setTextInteractionFlags(Qt.TextSelectableByMouse)
        pub5_link = QLabel('<a href=https://doi.org/10.1109/JPROC.2011.2106190>'
                           'doi:10.1109/JPROC.2011.2106190</a>')
        pub5_link.setOpenExternalLinks(True)
        pub5_link.setTextInteractionFlags(Qt.TextSelectableByMouse | Qt.LinksAccessibleByMouse)
        pub5_link.setStyleSheet('font-size: 13px; font: "Arial"; padding: 0px 0px 0px 34px;')
        self.verticalLayout.insertWidget(20, pub5_desc_a)
        self.verticalLayout.insertWidget(21, pub5_desc_b)
        self.verticalLayout.insertWidget(22, pub5_link)
        self.verticalLayout.insertWidget(23, QLabel(''))

        # add some more space
        self.verticalLayout.insertWidget(2, QLabel(''))
        self.verticalLayout.insertWidget(2, QLabel(''))

        ########

        """icon = QLabel()
        icon.setAlignment(Qt.AlignLeft)
        parent_container.insertWidget(3, icon)
        parent_container.setSpacing(4)"""


class ContactUsWindow(QMainWindow, About_Ui):
    def __init__(self, ctx, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ctx = ctx
        self.setupUi(self)

        # set the title
        self.setWindowTitle("PARSE - Contact Us")

        # set text to be selectable
        set_text_selectable(self)

        # connect UI elements using slots and signals
        self.pushButton.clicked.connect(self.back_to_menu)

        self.label.setText("To contact the developer via email or GitHub,\n"
                           "please use the following links:")

        # provide link to email
        self.label_2.setOpenExternalLinks(True)
        self.label_2.setText(
            "<a href=paulsirri@gmail.com>paulsirri@gmail.com</a>")
        self.label_2.setTextInteractionFlags(Qt.TextSelectableByMouse | Qt.LinksAccessibleByMouse)

        # provide link to GitHub
        self.label_3.setOpenExternalLinks(True)
        self.label_3.setText(
            "<a href=https://github.com/PARSE-team/PARSE>https://github.com/PARSE-team/PARSE</a>")
        self.label_3.setTextInteractionFlags(Qt.TextSelectableByMouse | Qt.LinksAccessibleByMouse)

        # center the window
        center_window(self)

    def back_to_menu(self):
        self.start_window = StartWindow(self.ctx)
        self.start_window.show()
        self.close()


class UserdefinedWindow(QMainWindow, Userdefined_Ui):
    def __init__(self, ctx, source, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ctx = ctx
        self.setupUi(self)

        # set the title
        self.setWindowTitle("PARSE - User Dataset")

        # set text to be selectable
        set_text_selectable(self)

        # set tooltip descriptions for user input parameters
        self.set_tooltips()

        # center window
        center_window(self)

        # set spin boxes to ignore scroll events, so user doesn't change them accidentally
        prevent_accidental_scroll_adjustments(self)

        # adjust layout
        self.lbl_instructions.setAlignment(Qt.AlignHCenter)
        self.label.setAlignment(Qt.AlignHCenter)

        # save session variables
        self.source = source

        # information to request from user
        self.rcp_path = None
        self.lcp_path = None
        self.dt_occ = None
        self.radius_target = None
        self.altitude_sc = None
        self.band_name = None
        # default value
        self.spin_bandfreq.setValue(8400)
        self.spin_occ_duration.setValue(10)

        # custom QLineEdit widgets that open a file dialogue when clicked
        self.custom_lineedit_rcp = ClickableLineEditWidget(' / User / directory / RCP_data. txt')
        self.gridLayout.addWidget(self.custom_lineedit_rcp, 0, 1)
        self.custom_lineedit_lcp = ClickableLineEditWidget(' / User / directory / LCP_data. txt')
        self.gridLayout.addWidget(self.custom_lineedit_lcp, 1, 1)

        # connect signals and slots
        self.custom_lineedit_rcp.clicked.connect(self.get_rcp_path)
        self.custom_lineedit_lcp.clicked.connect(self.get_lcp_path)
        self.btn_back.clicked.connect(self.back_to_start)
        self.btn_continue.clicked.connect(self.show_file_selection_window)
        # tooltips
        children = self.findChildren(QLabelClickable)
        for child in children:
            child.clicked.connect(show_tooltip_on_click)

    def get_rcp_path(self):
        # todo: "try:"
        self.rcp_path = QFileDialog.getOpenFileName()[0]
        if self.rcp_path:
            print("chose RCP file: " + str(self.rcp_path))
            self.custom_lineedit_rcp.setText(self.rcp_path)
        else:
            print("directory error")

    def get_lcp_path(self):
        self.lcp_path = QFileDialog.getOpenFileName()[0]
        if self.lcp_path:
            print("chose LCP file: " + str(self.lcp_path))
            self.custom_lineedit_lcp.setText(self.lcp_path)
        else:
            print("directory error")

    def back_to_start(self):
        self.start_window = StartWindow(self.ctx)
        self.start_window.show()
        self.close()

    def show_file_selection_window(self):
        print('\n\nrcp_path: ', self.rcp_path)
        print('lcp_path: ', self.lcp_path)
        print('band_name: ', self.band_name)
        # read inputs to "Acquisition Geometry"
        self.dt_occ = round(self.spin_occ_duration.value() * 60)
        self.radius_target = int(self.spin_eq_radius.value() * 1000)
        self.altitude_sc = int(self.spin_lowest_alt.value() * 1000)
        self.band_name = int(self.spin_bandfreq.value())

        self.file_window = FileWindowStandard(self.ctx, source=self.source,
                                              path_rcp=self.rcp_path,
                                              path_lcp=self.lcp_path,
                                              dt_occ=self.dt_occ,
                                              radius_target=self.radius_target,
                                              altitude_sc=self.altitude_sc,
                                              band_name=self.band_name)
        self.file_window.show()
        self.close()

    def set_min_and_max_limits(self):
        # todo: implement
        """maximum_seconds = np.floor((self.rcp_file.stop_time
                                    - self.rcp_file.start_time).to_value('sec')
                                   - self.current_settings.seconds_for_welch)
        maximum_seconds = TimeDelta(maximum_seconds, format='sec')
        max_datetime = (self.rcp_file.start_time + maximum_seconds).strf('')"""
        pass

    def set_tooltips(self):

        descriptions = {
            'lbl_occ_duration': 'typically 1 min - 30 min or longer',
            'band_freq': 'frequency used to transmit data',
            'lbl_lowest_alt': 'spacecraft distance above target surface'
        }

        self.add_info_icon(parent_container=self.horizontalLayout_6,
                           parameter_description=descriptions['lbl_occ_duration'])
        self.add_info_icon(parent_container=self.horizontalLayout_8,
                           parameter_description=descriptions['lbl_lowest_alt'])
        self.add_info_icon(parent_container=self.horizontalLayout_9,
                           parameter_description=descriptions['band_freq'])

    def add_info_icon(self, parent_container=None, parameter_description=None):
        # retrieve the info icon image from resources and resize it
        pixmap_icon = QPixmap(QImage(self.ctx.img_info_icon()))
        pixmap_icon = pixmap_icon.scaled(
            18, 18, Qt.KeepAspectRatio, Qt.SmoothTransformation)

        # make an empty label widget to use as a canvas
        icon = QLabelClickable()

        # set the icon image
        icon.setPixmap(pixmap_icon)
        icon.setAlignment(Qt.AlignLeft)

        # set the string description of the parameter
        icon.setToolTip(parameter_description)

        if parent_container is self.horizontalLayout_2:
            icon.setAlignment(Qt.AlignLeft)
            parent_container.insertWidget(3, icon)
            parent_container.setSpacing(4)
        else:
            parent_container.insertWidget(1, icon)
            parent_container.setSpacing(4)


class ClickableLineEditWidget(QLineEdit):
    """ A custom QWidget that emits a signal when clicked. """

    clicked = QtCore.pyqtSignal()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.clicked.emit()
        else:
            super().mousePressEvent(event)


class FileWindowDetachedLabel(QMainWindow, File_Ui_DetachedLabel):
    def __init__(self, ctx, source, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ctx = ctx
        self.setupUi(self)

        # set the title
        self.setWindowTitle("PARSE - File Selection")

        # set text to be selectable
        set_text_selectable(self)

        # set window size
        w = round(1920 * 0.75)
        h = round(1080 * 0.75)
        self.resize(w, h)

        # center window
        center_window(self)

        # save session variables
        self.source = source

        # read label files in directory, add to selection table
        self.data_labels = get_files(source, self.ctx)
        self.fill_table()

        # when a row is clicked, pass file info to next window
        self.table_files.itemSelectionChanged.connect(self.display_label)

        # keep track over which file the user highlighted
        self.selected_file = None

        # connect buttons
        self.btn_back.clicked.connect(self.back_to_start)
        self.btn_process.clicked.connect(self.show_signal_window)

    def fill_table(self):
        # format table
        # self.table_files.setFont(QFont("Courier", 13))
        # self.lbl_quickview.setFont(QFont("Courier", 13))
        column_names = ['File Name', 'Start Time', 'Stop Time', 'Band', 'Polarization']
        self.table_files.setColumnCount(5)
        # add one row for every LCP/RCP file pair
        items_count = len(self.data_labels)
        if items_count % 2 == 1:
            items_count += 1
        self.table_files.setRowCount(items_count / 2)
        self.table_files.setHorizontalHeaderLabels(column_names)

        # only add files as pairs
        already_added = []

        # fill with file metadata
        for row in range(self.table_files.rowCount()):
            for dl in self.data_labels:
                if dl.file_name not in already_added:
                    # add metadata for both RCP and LCP data pairs
                    polar_partner = get_polar_compliment(dl, self.data_labels)
                    already_added.append(dl.file_name)
                    already_added.append(polar_partner.file_name)
                    # set values for each item in row
                    self.table_files.setItem(row, 0, QTableWidgetItem(
                        dl.file_name + '\n' + polar_partner.file_name))
                    self.table_files.setItem(row, 1, QTableWidgetItem(strftime_yyyyDOYhhmmss(
                        dl.start_time) + '\n' + strftime_yyyyDOYhhmmss(polar_partner.start_time)))
                    self.table_files.setItem(row, 2, QTableWidgetItem(strftime_yyyyDOYhhmmss(
                        dl.stop_time) + '\n' + strftime_yyyyDOYhhmmss(polar_partner.stop_time)))
                    self.table_files.setItem(row, 3, QTableWidgetItem(
                        dl.band_name + '\n' + polar_partner.band_name))
                    self.table_files.setItem(row, 4, QTableWidgetItem(
                        dl.polarization + '\n' + polar_partner.polarization))
                    break
            for col in range(self.table_files.columnCount()):
                self.table_files.setRowHeight(row, 50)

        # set QTableWidget formatting properties
        self.table_files.resizeColumnsToContents()
        self.table_files.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table_files.setSelectionMode(QAbstractItemView.SingleSelection)
        self.table_files.setEditTriggers(QTableWidget.NoEditTriggers)

    def display_label(self):
        for lbl in self.data_labels:
            if lbl.file_name in self.table_files.selectedItems()[0].text():
                # the selected row matches a data_label object
                self.selected_file = lbl
                # some missions may not use label files
                if lbl.path_to_label:
                    # read the label file, print to UI
                    f = open(lbl.path_to_label, 'r')
                    file_contents = f.read()
                    f.close()
                    self.lbl_quickview.setText(file_contents)

    def back_to_start(self):
        self.start_window = StartWindow(self.ctx)
        self.start_window.show()
        self.close()

    def show_signal_window(self):
        self.files_tuple = find_polar_pair(self.selected_file, self.data_labels)
        self.signal_window = SignalWindow(self.ctx, self.source, self.files_tuple)
        self.signal_window.show()
        self.close()


class FileWindowStandard(QMainWindow, File_Ui_Standard):
    def __init__(self, ctx, source, path_rcp=None, path_lcp=None, dt_occ=None, radius_target=None,
                 altitude_sc=None, band_name=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ctx = ctx
        self.setupUi(self)

        # set the title
        self.setWindowTitle("PARSE - File Selection")

        # set text to be selectable
        set_text_selectable(self)

        # set window size
        w = 800
        h = 600
        self.resize(w, h)

        # center window
        center_window(self)

        # save session variables
        self.source = source
        self.dt_occ = dt_occ
        self.radius_target = radius_target
        self.altitude_sc = altitude_sc

        # read label files in directory, add to selection table
        self.data_labels = get_files(source, self.ctx, path_rcp=path_rcp, path_lcp=path_lcp,
                                     band_name=band_name)
        self.fill_table()

        # when a row is clicked, pass file info to next window
        self.table_files.itemSelectionChanged.connect(self.display_label)

        # keep track over which file the user highlighted
        self.selected_file = None

        # connect buttons
        self.btn_back.clicked.connect(self.back_to_start)
        self.btn_process.clicked.connect(self.show_signal_window)

    def fill_table(self):
        # format table
        # self.table_files.setFont(QFont("Monospace", 13))
        # self.lbl_quickview.setFont(QFont("Monospace", 12))
        column_names = ['File Name', 'Start Time', 'Stop Time', 'Band', 'Polarization']
        self.table_files.setColumnCount(5)
        # add one row for every LCP/RCP file pair
        items_count = len(self.data_labels)
        if items_count % 2 == 1:
            items_count += 1
        self.table_files.setRowCount(items_count / 2)
        self.table_files.setHorizontalHeaderLabels(column_names)

        # only add files as pairs
        already_added = []

        # fill with file metadata
        for row in range(self.table_files.rowCount()):
            for dl in self.data_labels:
                if dl.file_name not in already_added:
                    # add metadata for both RCP and LCP data pairs
                    polar_partner = get_polar_compliment(dl, self.data_labels)
                    already_added.append(dl.file_name)
                    already_added.append(polar_partner.file_name)
                    # set values for each item in row
                    self.table_files.setItem(row, 0, QTableWidgetItem(
                        dl.file_name + '\n' + polar_partner.file_name))
                    self.table_files.setItem(row, 1, QTableWidgetItem(strftime_yyyyDOYhhmmss(
                        dl.start_time) + '\n' + strftime_yyyyDOYhhmmss(polar_partner.start_time)))
                    self.table_files.setItem(row, 2, QTableWidgetItem(strftime_yyyyDOYhhmmss(
                        dl.stop_time) + '\n' + strftime_yyyyDOYhhmmss(polar_partner.stop_time)))
                    self.table_files.setItem(row, 3, QTableWidgetItem(
                        dl.band_name + '\n' + polar_partner.band_name))
                    self.table_files.setItem(row, 4, QTableWidgetItem(
                        dl.polarization + '\n' + polar_partner.polarization))
                    break
            for col in range(self.table_files.columnCount()):
                self.table_files.setRowHeight(row, 50)

        # set QTableWidget formatting properties
        self.table_files.resizeColumnsToContents()
        self.table_files.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table_files.setSelectionMode(QAbstractItemView.SingleSelection)
        self.table_files.setEditTriggers(QTableWidget.NoEditTriggers)

    def display_label(self):
        for lbl in self.data_labels:
            if lbl.file_name in self.table_files.selectedItems()[0].text():
                # the selected row matches a data_label object
                self.selected_file = lbl
                # some missions may not use label files
                if lbl.path_to_label:
                    # read the label file, print to UI
                    f = open(lbl.path_to_label, 'r')
                    file_contents = f.read()
                    f.close()
                    self.lbl_quickview.setText(file_contents)

    def back_to_start(self):
        self.start_window = StartWindow(self.ctx)
        self.start_window.show()
        self.close()

    def show_signal_window(self):
        if self.dt_occ and self.radius_target and self.altitude_sc:
            # the user defined own data, these are the parameters they entered
            userdefined_params = (self.dt_occ, self.radius_target, self.altitude_sc)
        else:
            # the user has chosen a bundled dataset, use the default parameters
            userdefined_params = None

        # make a SignalWindow using the selected dataset and its polar pair
        self.files_tuple = find_polar_pair(self.selected_file, self.data_labels)
        self.signal_window = SignalWindow(self.ctx, self.source, self.files_tuple,
                                          userdefined_params)
        self.signal_window.show()
        self.close()


class SignalWindow(QMainWindow, Signal_Ui):
    signal_to_run_worker = QtCore.pyqtSignal(object, object, object)
    signal_to_plot_analysis_results = QtCore.pyqtSignal(object)
    signal_to_hide_analysis_results = QtCore.pyqtSignal()

    def __init__(self, ctx, source, files_tuple, userdefined_params=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ctx = ctx
        self.setupUi(self)

        # set the title
        self.setWindowTitle("PARSE - Processing and Analysis")

        # set text to be selectable
        set_text_selectable(self)

        # set tooltip descriptions for user input parameters
        self.set_tooltips()

        # set window size
        w = round(1920 * 0.80)
        h = round(1080 * 0.80)
        self.resize(w, h)

        # center the window
        center_window(self)

        # set the default active tab to "Signal Processing"
        self.tab_widget.setCurrentIndex(0)
        # self.tab_widget.setTabEnabled(1, False)

        # set spin boxes to ignore scroll events, so user doesn't change them accidentally
        prevent_accidental_scroll_adjustments(self)

        self.tab_widget.setMinimumWidth(523)

        # format text labels in the interface
        self.format_text_in_gui()

        # add a toolbar for Matplotlib
        self.setup_plotting_toolbar()

        # create a WorkerDataIngestion object and a thread
        self.worker_dataingestion = WorkerDataIngestion()
        self.worker_dataingestion_thread = QtCore.QThread()

        # assign the worker_dataingestion to the thread and start the thread
        self.worker_dataingestion.moveToThread(self.worker_dataingestion_thread)
        self.worker_dataingestion_thread.start()

        # dialog box to show worker progress
        self.progress_window = IngestionProgress(self.ctx, parent=self)
        # self.progress_window.setFocus(True)
        # self.progress_window.raise_()
        # self.progress_window.activateWindow()

        # connect signals to slots AFTER moving the object to the thread
        self.connect_signals_to_slots()

        # save current source
        self.source = source

        # unpack selected files
        self.rcp_file, self.lcp_file = files_tuple

        # instantiate static attributes that will be returned by worker
        self.rcp_processed = None
        self.lcp_processed = None
        self.rcp_data = None
        self.lcp_data = None
        self.sample_rate = None

        # instantiate signal processing parameters
        self.current_settings = None
        self.current_settings_rounded = None

        # instantiate signal analysis parameters
        self.msmt = None

        # worker thread processes and returns plotting/animation data
        self.signal_to_run_worker.emit(self.rcp_file, self.lcp_file, userdefined_params)

    def show_parameters(self, s):
        """ A method to set the current value for input widgets on the Signal Processing tab. """

        # row 1 of group: "Acquisition Geometry"
        self.line_edit_target.setText(s.target)
        self.line_edit_mission.setText(s.mission)
        # row 2 of group: "Acquisition Geometry"
        self.spin_occ_duration.setValue(np.floor(s.dt_occ / 60))
        self.spin_eq_radius.setValue(np.floor(s.radius_target / 1000))
        # row 3 of group: "Acquisition Geometry"
        self.spin_sc_velocity.setValue(s.v_sc_orbital)
        self.spin_lowest_alt.setValue(np.floor(s.altitude_sc / 1000))

        # row 1 of group: "Signal Processing Parameters"
        self.spin_freq_separation.setValue(s.df_calc)
        self.spin_freq_res.setValue(s.freq_res)
        # row 2 of group: "Signal Processing Parameters"
        self.spin_l_win.setValue(s.samples_per_raw_fft)
        self.spin_t_int.setValue(s.seconds_per_raw_fft)
        # row 3 of group: "Signal Processing Parameters"
        self.spin_k_spec.setValue(s.raw_fft_per_average)
        self.spin_timespan.setValue(s.seconds_for_welch)
        # row 4 of group: "Signal Processing Parameters"
        self.spin_moving_overlap.setValue(s.percent_window_per_hop)
        self.spin_t_hop.setValue(s.seconds_per_hop)

        # row 1 of group: "Animation Playback"
        # display the start time of the animation
        datetime_as_astropy = self.rcp_file.start_time + TimeDelta(s.start_sec_user, format='sec')
        datetime_as_pyqt = convert_astropy_to_pyqt(datetime_as_astropy)
        self.dateTimeEdit.setDateTime(datetime_as_pyqt)
        self.dateTimeEdit.setDisplayFormat('hh:mm:ss')
        self.spin_doy.setValue(int(datetime_as_pyqt.date().dayOfYear()))
        # display animation speed
        self.spin_ani_speed.setMaximum(3)
        self.spin_ani_speed.setValue(round(1000 / s.interval, 2))

        # row 1 of group: "Plot Window Properties"
        self.spin_xmin.setValue(s.xlim_min)
        self.spin_xmax.setValue(s.xlim_max)
        # row 2 of group: "Plot Window Properties"
        self.spin_ymin.setValue(s.ylim_min)
        self.spin_ymax.setValue(s.ylim_max)

        # make a copy of these rounded values, in order to keep track of changes made by user
        self.current_settings_rounded = {
            'line_edit_target': self.line_edit_target.text(),
            'line_edit_mission': self.line_edit_mission.text(),
            'spin_occ_duration': self.spin_occ_duration.value(),
            'spin_eq_radius': self.spin_eq_radius.value(),
            'spin_sc_velocity': self.spin_sc_velocity.value(),
            'spin_lowest_alt': self.spin_lowest_alt.value(),
            'spin_freq_separation': self.spin_freq_separation.value(),
            'spin_freq_res': self.spin_freq_res.value(),
            'spin_l_win': self.spin_l_win.value(),
            'spin_t_int': self.spin_t_int.value(),
            'spin_k_spec': self.spin_k_spec.value(),
            'spin_timespan': self.spin_timespan.value(),
            'spin_moving_overlap': self.spin_moving_overlap.value(),
            'spin_t_hop': self.spin_t_hop.value(),
            'spin_xmin': self.spin_xmin.value(),
            'spin_xmax': self.spin_xmax.value(),
            'spin_ymin': self.spin_ymin.value(),
            'spin_ymax': self.spin_ymax.value(),
            'spin_doy': self.spin_doy.value(),
            'dateTimeEdit': self.dateTimeEdit.dateTime(),
            'spin_ani_speed': self.spin_ani_speed.value(),
        }

    def apply_changes(self):
        """ A method to read the user input parameters from QSpinBox widgets on
        the Signal Processing tab, generate a new SignalProcessing object, then pass
        these new settings into the animation widget for plotting.

        NOTE: Some of the values had to be rounded when they were initially printed
        to the Signal Processing tab. So, when reading these values back in, the
        values can't be copied exactly, as precision may have been lost to rounding.
        To address this issue, the code below measures the amount by which the user
        changed each parameter, then adds this difference to the initial value.

        Example:
        new_value_in_code = ( new_value_in_GUI - old_value_in_GUI ) + old_value_in_code

        """

        # signals to stop generating old plots
        self.animation_widget.pause_worker()
        self.animation_widget.kill_worker()

        # ensure the old data has been cleared from queues
        self.animation_widget.plots = []
        self.animation_widget.frame_index = 0

        # row 1 of group: "Acquisition Geometry"
        target = self.line_edit_target.text()
        mission = self.line_edit_mission.text()
        # row 2 of group: "Acquisition Geometry"
        dt_occ = round(((self.spin_occ_duration.value() - self.current_settings_rounded[
            'spin_occ_duration']) * 60) + self.current_settings.dt_occ)
        radius_target = ((self.spin_eq_radius.value() - self.current_settings_rounded[
            'spin_eq_radius']) * 1000) + self.current_settings.radius_target
        # row 3 of group: "Acquisition Geometry"
        v_sc_orbital = (self.spin_sc_velocity.value() - self.current_settings_rounded[
            'spin_sc_velocity']) + self.current_settings.v_sc_orbital
        altitude_sc = ((self.spin_lowest_alt.value() - self.current_settings_rounded[
            'spin_lowest_alt']) * 1000) + self.current_settings.altitude_sc

        # row 1 of group: "Signal Processing Parameters"
        # NOT ADJUSTABLE: df_calc = (self.spin_freq_separation.value())
        freq_res = (self.spin_freq_res.value() - self.current_settings_rounded[
            'spin_freq_res']) + self.current_settings.freq_res
        # row 2 of group: "Signal Processing Parameters"
        # NOT ADJUSTABLE:  samples_per_raw_fft = (self.spin_l_win.value())
        # NOT ADJUSTABLE: seconds_per_raw_fft = (self.spin_t_int.value())
        # row 3 of group: "Signal Processing Parameters"
        raw_fft_per_average = round((self.spin_k_spec.value() - self.current_settings_rounded[
            'spin_k_spec']) + self.current_settings.raw_fft_per_average)
        # handle specially, seconds_for_welch is dependent on, and a dependent of, other parameters
        if self.spin_timespan.value() != self.current_settings_rounded['spin_timespan']:
            # user manually entered value for seconds_for_welch, use to calculate other params
            seconds_for_welch_user = (self.spin_timespan.value() - self.current_settings_rounded[
                'spin_timespan']) + self.current_settings.seconds_for_welch
        else:
            # user did not adjust seconds_for_welch, just use defaults in calculations
            seconds_for_welch_user = None
        # row 4 of group: "Signal Processing Parameters"
        percent_window_per_hop = (self.spin_moving_overlap.value() - self.current_settings_rounded[
            'spin_moving_overlap']) + self.current_settings.percent_window_per_hop
        # NOT ADJUSTABLE : seconds_per_hop = (self.spin_t_hop.value())

        # row 1a of group: "Animation Playback"
        # the user's requested start time, as a PyQt5 QDateTime() instance
        datetime_as_pyqt = self.get_requested_start_time()
        # the user's requested start time, as an Astropy Time() instance
        datetime_as_astropy = convert_pyqt_to_astropy(datetime_as_pyqt)
        # the user's requested start time, as number of seconds since beginning of file
        start_sec_user = round((datetime_as_astropy - self.rcp_file.start_time).to_value('sec'))
        # row 1b of group: "Animation Playback"
        # convert fps to milliseconds
        frames_per_second = self.spin_ani_speed.value()
        interval = round(1000 / frames_per_second)

        # row 1 of group: "Plot Window Properties"
        xlim_min = (self.spin_xmin.value() - self.current_settings_rounded[
            'spin_xmin']) + self.current_settings.xlim_min
        xlim_max = (self.spin_xmax.value() - self.current_settings_rounded[
            'spin_xmax']) + self.current_settings.xlim_max
        # row 2 of group: "Plot Window Properties"
        ylim_min = (self.spin_ymin.value() - self.current_settings_rounded[
            'spin_ymin']) + self.current_settings.ylim_min
        ylim_max = (self.spin_ymax.value() - self.current_settings_rounded[
            'spin_ymax']) + self.current_settings.ylim_max

        # make new instance of SignalProcessing
        # get all parameters for radar analysis pipeline, using RCP file to set default values
        new_settings = get_signal_processing_parameters(
            filenames=(self.rcp_file.file_name, self.lcp_file.file_name),
            rcp_data=self.rcp_data,
            lcp_data=self.lcp_data,
            sample_rate=self.sample_rate,
            band_name=self.rcp_file.band_name,
            global_time=self.rcp_file.start_time,
            target=target, mission=mission,
            dt_occ=dt_occ, radius_target=radius_target,
            v_sc_orbital=v_sc_orbital, altitude_sc=altitude_sc,
            df_calc=None, freq_res=freq_res,
            samples_per_raw_fft=None, seconds_per_raw_fft=None,
            raw_fft_per_average=raw_fft_per_average,
            seconds_for_welch_user=seconds_for_welch_user,
            percent_window_per_hop=percent_window_per_hop,
            seconds_per_hop=None,
            xlim_min=xlim_min, xlim_max=xlim_max,
            ylim_min=ylim_min, ylim_max=ylim_max,
            start_sec_user=start_sec_user, interval=interval,
            file_start_time=self.rcp_file.start_time,
            file_end_time=self.rcp_file.stop_time,
            did_calculate_overview=True,
            old_settings=self.current_settings)

        # keep track of current settings
        self.current_settings = new_settings

        # show new parameters to user
        self.show_parameters(new_settings)

        # pass new parameters into animation widget, initialize plot
        self.setup_animation(new_settings, self.rcp_data, self.lcp_data)

    def show_parameters_plot_analysis(self, msmt):
        """ A method to set the value of each QSpinBox widget on the Spectral Analysis tab. """

        self.spin_measure_bandwidth_below.setValue(msmt.NdB_below)
        self.spin_x_min.setValue(msmt.freq_local_min)
        self.spin_x_max.setValue(msmt.freq_local_max)

        self.spin_ymax_global.setValue(msmt.Pxx_max_RCP)
        self.spin_ymax_global_LCP.setValue(msmt.Pxx_LCP_at_max)
        self.spin_x_at_ymax_global.setValue(msmt.freq_at_max)
        self.spin_bandwidth_global.setDecimals(1)
        self.spin_bandwidth_global.setValue(msmt.bandwidth_RCP_at_max)
        self.spin_bandwidth_global_LCP.setDecimals(1)
        self.spin_bandwidth_global_LCP.setValue(msmt.bandwidth_LCP_at_max)
        self.spin_noise_variance_global.setValue(msmt.Pxx_noise_var_RCP)
        self.spin_noise_variance_global_LCP.setValue(msmt.Pxx_noise_var_LCP)
        self.spin_delta_x_predict.setValue(msmt.df_calc)

        self.spin_ymax_local.setValue(msmt.Pxx_local_max_RCP)
        self.spin_ymax_local_LCP.setValue(msmt.Pxx_LCP_at_local_max)
        self.spin_x_at_ymax_local.setValue(msmt.freq_at_local_max)
        self.spin_bandwidth_local.setDecimals(1)
        self.spin_bandwidth_local.setValue(msmt.bandwidth_RCP_local_max)
        self.spin_bandwidth_local_LCP.setDecimals(1)
        self.spin_bandwidth_local_LCP.setValue(msmt.bandwidth_LCP_local_max)
        self.spin_delta_y.setValue(msmt.delta_Pxx_max_RCP)
        self.spin_delta_y_LCP.setValue(msmt.delta_Pxx_LCP)
        self.spin_delta_x_observed.setValue(msmt.df_obsv)

    def apply_changes_plot_analysis(self):
        """ A method to read the user input parameters from QSpinBox widgets
        on the Signal Analysis tab, generate a new SpectralAnalysis object, then
        pass these results into the animation widget. """

        NdB_below = int(round(self.spin_measure_bandwidth_below.value()))
        freq_local_min = int(round(self.spin_x_min.value()))
        freq_local_max = int(round(self.spin_x_max.value()))

        # get measurements for plot analysis, using data from RCP file
        msmt = get_spectral_analysis_results(
            s=self.animation_widget.s,
            freqs=self.animation_widget.plots[self.animation_widget.frame_index][0],
            Pxx=self.animation_widget.plots[self.animation_widget.frame_index][1],
            freqs_LCP=self.animation_widget.plots[self.animation_widget.frame_index][2],
            Pxx_LCP=self.animation_widget.plots[self.animation_widget.frame_index][3],
            NdB_below=NdB_below, freq_local_min=freq_local_min,
            freq_local_max=freq_local_max)

        self.msmt = msmt

        # show new parameters to user
        self.show_parameters_plot_analysis(msmt)

        # show annotations on plot
        self.signal_to_plot_analysis_results.emit(msmt)

        # provide error messages to help user diagnose issues
        if self.msmt.error_NdB_below:
            self.show_error_message('Error: Cannot measure bandwidth at noise levels. '
                                    'Please measure bandwidth higher on the peak.')
        if self.msmt.error_global_RCP:
            self.show_error_message('Warning: No signal detected in RCP data; peak '
                                    'detectability limit is at least 3 dB above the noise.')
        if self.msmt.error_global_LCP:
            self.show_error_message('Warning: No signal detected in LCP data; peak '
                                    'detectability limit is at least 3 dB above the noise.')
        if self.msmt.error_local_RCP:
            self.show_error_message('Warning: No signal detected in selected '
                                    'range of RCP data; peak detectability limit '
                                    'is at least 3 dB above the noise.')
        if self.msmt.error_local_LCP:
            self.show_error_message('Warning: No signal detected in selected '
                                    'range of LCP data; peak detectability limit '
                                    'is at least 3 dB above the noise.')
        if self.msmt.error_finding_bandwidth:
            self.show_error_message('Error: Unable to measure the bandwidth of the specified '
                                    'peak. Bandwidth will be set to 0 Hz.')

    def toggle_results(self):
        print("\nSignalWindow.toggle_results()\n")
        if self.tab_widget.currentIndex() == 1:
            # get measurements for plot analysis using data from current RCP frame, use defaults
            self.msmt = get_spectral_analysis_results(
                s=self.animation_widget.s,
                freqs=self.animation_widget.plots[self.animation_widget.frame_index][0],
                Pxx=self.animation_widget.plots[self.animation_widget.frame_index][1],
                freqs_LCP=self.animation_widget.plots[self.animation_widget.frame_index][2],
                Pxx_LCP=self.animation_widget.plots[self.animation_widget.frame_index][3])

            # print values to QSpinBoxes on Signal Analysis tab
            self.show_parameters_plot_analysis(self.msmt)

            # show annotations on plot
            self.signal_to_plot_analysis_results.emit(self.msmt)

            # provide error messages to help user diagnose issues
            if self.msmt.error_NdB_below:
                self.show_error_message('Error: Cannot measure bandwidth at noise levels. '
                                        'Please measure bandwidth higher on the peak.')
            if self.msmt.error_global_RCP:
                self.show_error_message('Warning: No signal detected in RCP data; peak '
                                        'detectability limit is at least 3 dB above the noise.')
            if self.msmt.error_global_LCP:
                self.show_error_message('Warning: No signal detected in LCP data; peak '
                                        'detectability limit is at least 3 dB above the noise.')
            if self.msmt.error_local_RCP:
                self.show_error_message('Warning: No signal detected in selected '
                                        'range of RCP data; peak detectability limit '
                                        'is at least 3 dB above the noise.')
            if self.msmt.error_local_LCP:
                self.show_error_message('Warning: No signal detected in selected '
                                        'range of LCP data; peak detectability limit '
                                        'is at least 3 dB above the noise.')
            if self.msmt.error_finding_bandwidth:
                self.show_error_message('Error: Unable to measure the bandwidth of the specified '
                                        'peak. Bandwidth will be set to 0 Hz.')

        elif self.tab_widget.currentIndex() == 0:
            # hide results
            print("hide results")
            self.signal_to_hide_analysis_results.emit()

    def setup_animation(self, s, rcp_data, lcp_data):
        print("\nSignalWindow.setup_animation()")
        self.animation_widget.setup(s, rcp_data, lcp_data)
        # TODO: QDialog to ask if the user wants to reset the currently running animation

    def play_animation(self):
        print("\nSignalWindow.play_animation()")
        self.animation_widget.play()

        # only allow the user to analyze a plot if the animation is paused
        self.tab_widget.setTabEnabled(1, False)

    def pause_animation(self):
        print("\nSignalWindow.pause_animation()")
        self.animation_widget.pause()

        # only allow the user to analyze a plot if the animation is paused
        self.tab_widget.setTabEnabled(1, True)

    def export_plot(self):
        rcp_x, rcp_y, lcp_x, lcp_y, files_label, time_label, current_index, \
        current_second = self.animation_widget.plots[self.animation_widget.frame_index]
        self.export_window = ExportWindow(self.ctx, rcp_x=rcp_x, rcp_y=rcp_y, lcp_x=lcp_x,
                                          lcp_y=lcp_y, fig=self.animation_widget.fig)
        self.export_window.show()

    def back_to_files(self):
        print('SignalWindow.back_to_files(self)')
        self.pause_animation()
        self.back_to_window = None
        if self.source == 'rosetta':
            self.back_to_window = FileWindowDetachedLabel(self.ctx, self.source)
        elif self.source == 'dawn':
            self.back_to_window = FileWindowStandard(self.ctx, self.source)
        elif self.source == 'userfile':
            self.back_to_window = StartWindow(self.ctx)
        self.back_to_window.show()
        self.close()

    def show_error_message(self, message):
        error_dialog = QtWidgets.QErrorMessage()
        error_dialog.setWindowModality(QtCore.Qt.WindowModal)
        error_dialog.showMessage(message)
        error_dialog.exec_()

    def seconds_to_dayshours(self, seconds):
        # days
        days = seconds // 86400
        # remaining seconds
        seconds = seconds - (days * 86400)
        # hours
        hours = seconds // 3600
        # remaining seconds
        seconds = seconds - (hours * 3600)
        # minutes
        minutes = seconds // 60
        # remaining seconds
        seconds = seconds - (minutes * 60)
        return int(days), int(hours)

    def get_requested_start_time(self):
        # get the requested start time, not accounting for date change
        partial_datetime_pyqt = self.dateTimeEdit.dateTime()
        # calculate how much the user changed the date
        new_day_of_year = int(self.spin_doy.value())
        old_day_of_year = partial_datetime_pyqt.date().dayOfYear()
        doy_change = new_day_of_year - old_day_of_year
        # add the date change
        datetime_pyqt = partial_datetime_pyqt.addDays(doy_change)
        return datetime_pyqt

    def set_min_and_max_limits(self):
        # todo: implement
        """maximum_seconds = np.floor((self.rcp_file.stop_time
                                    - self.rcp_file.start_time).to_value('sec')
                                   - self.current_settings.seconds_for_welch)
        maximum_seconds = TimeDelta(maximum_seconds, format='sec')
        max_datetime = (self.rcp_file.start_time + maximum_seconds).strf('')"""
        pass

    def set_tooltips(self):
        """ A function to define the tooltip descriptions for user input parameters,
        then assign each description to its corresponding QWidget. """

        descriptions = {
            'lbl_occ_duration': 'typically 1 min - 30 min or longer',
            'lbl_sc_velocity': 'spacecraft orbital / flyby speed',
            'lbl_lowest_alt': 'spacecraft distance above target surface',
            'lbl_freq_separation': 'computed frequency difference between direct and echo signals',
            'lbl_freq_res': 'frequency resolution of the output plots',
            'lbl_l_win': 'number of data points over which to perform an FFT '
                         '(calculated from f_res)',
            'lbl_t_int': 'FFT integration time',
            'lbl_k_spec': "number of FFT's to average together",
            'lbl_timespan': 'timespan of each frame produced on right',
            'lbl_moving_overlap': 'step-size between each moving average window '
                                  '(percentage of window size)',
            'lbl_t_hop': 'calculated increment between each successive moving average window',
            'lbl_start_sec': 'use the overview plot as a reference in choosing the start time',
            'label_2': 'peak widths can be compared when measured at the same dB below '
                       'their peak (e.g., comparing their "10-dB bandwidth")',
            'label_20': 'select the frequency range containing a potential echo signal '
                        'but not the direct signal',
            'label_6': 'peak power in RCP (dB)',
            'label_7': 'frequency (Hz) of the main peak',
            'label_8': 'frequency width of the main peak (measured at N-dB below the peak)',
            'label_9': 'detectable signal peaks are defined as being at least 3 dB greater '
                       'than this noise level',
            'label_10': 'the calculated, expected frequency difference between the direct '
                        'and echo peaks',
            'label_12': 'local maximum RCP power (dB) in the selected range',
            'label_13': 'center frequency (Hz) of the peak in the selected range',
            'label_14': 'frequency width of the secondary RCP peak identified in the selected '
                        'frequency range',
            'label_16': 'difference in peak power of the two selected maxima (dB)',
            'label_17': 'observed frequency difference between the two selected '
                        'peaks (should be close to δf calc if the two peaks are '
                        'accurately identified as the direct and echo signals)'
        }

        self.add_info_icon(parent_container=self.horizontalLayout_10,
                           parameter_description=descriptions['lbl_occ_duration'])
        self.add_info_icon(parent_container=self.horizontalLayout_11,
                           parameter_description=descriptions['lbl_sc_velocity'])
        self.add_info_icon(parent_container=self.horizontalLayout_12,
                           parameter_description=descriptions['lbl_lowest_alt'])
        self.add_info_icon(parent_container=self.horizontalLayout_13,
                           parameter_description=descriptions['lbl_freq_separation'])
        self.add_info_icon(parent_container=self.horizontalLayout_14,
                           parameter_description=descriptions['lbl_freq_res'])
        self.add_info_icon(parent_container=self.horizontalLayout_15,
                           parameter_description=descriptions['lbl_l_win'])
        self.add_info_icon(parent_container=self.horizontalLayout_16,
                           parameter_description=descriptions['lbl_t_int'])
        self.add_info_icon(parent_container=self.horizontalLayout_17,
                           parameter_description=descriptions['lbl_k_spec'])
        self.add_info_icon(parent_container=self.horizontalLayout_18,
                           parameter_description=descriptions['lbl_timespan'])
        self.add_info_icon(parent_container=self.horizontalLayout_19,
                           parameter_description=descriptions['lbl_moving_overlap'])
        self.add_info_icon(parent_container=self.horizontalLayout_20,
                           parameter_description=descriptions['lbl_t_hop'])
        self.add_info_icon(parent_container=self.horizontalLayout_21,
                           parameter_description=descriptions['lbl_start_sec'])

        self.add_info_icon(parent_container=self.horizontalLayout_2,
                           parameter_description=descriptions['label_2'])
        self.add_info_icon(parent_container=self.horizontalLayout_22,
                           parameter_description=descriptions['label_20'])
        self.add_info_icon(parent_container=self.horizontalLayout_23,
                           parameter_description=descriptions['label_6'])
        self.add_info_icon(parent_container=self.horizontalLayout_24,
                           parameter_description=descriptions['label_7'])
        self.add_info_icon(parent_container=self.horizontalLayout_25,
                           parameter_description=descriptions['label_8'])
        self.add_info_icon(parent_container=self.horizontalLayout_26,
                           parameter_description=descriptions['label_9'])
        self.add_info_icon(parent_container=self.horizontalLayout_27,
                           parameter_description=descriptions['label_10'])
        self.add_info_icon(parent_container=self.horizontalLayout_28,
                           parameter_description=descriptions['label_12'])
        self.add_info_icon(parent_container=self.horizontalLayout_29,
                           parameter_description=descriptions['label_13'])
        self.add_info_icon(parent_container=self.horizontalLayout_30,
                           parameter_description=descriptions['label_14'])
        self.add_info_icon(parent_container=self.horizontalLayout_31,
                           parameter_description=descriptions['label_16'])
        self.add_info_icon(parent_container=self.horizontalLayout_32,
                           parameter_description=descriptions['label_17'])

    def add_info_icon(self, parent_container=None, parameter_description=None):
        # retrieve the info icon image from resources and resize it
        # TODO: cache this resource using PyQt5 and FBS
        pixmap_icon = QPixmap(QImage(self.ctx.img_info_icon()))
        pixmap_icon = pixmap_icon.scaled(
            18, 18, Qt.KeepAspectRatio, Qt.SmoothTransformation)

        # make an empty label widget to use as a canvas
        icon = QLabelClickable()

        # set the icon image
        icon.setPixmap(pixmap_icon)
        icon.setAlignment(Qt.AlignLeft | Qt.AlignBottom)

        # set the string description of the parameter
        icon.setToolTip(parameter_description)

        if parent_container is self.horizontalLayout_2:
            icon.setAlignment(Qt.AlignLeft)
            parent_container.insertWidget(3, icon)
            parent_container.setSpacing(4)
        else:
            parent_container.insertWidget(1, icon)
            parent_container.setSpacing(4)

    def show_processing_tab(self):
        self.tab_widget.setCurrentIndex(0)

    def connect_signals_to_slots(self):
        """ A method to setup all PyQt5 signals/slot connections for this window during init. """

        # connect main thread and worker thread
        # connect the worker signals/slots AFTER moving worker object to thread (see init method)
        self.worker_dataingestion.signal_to_return_data.connect(self.receive_data_from_worker)
        self.worker_dataingestion.signal_progress.connect(self.progress_window.receive_progress)
        self.signal_to_run_worker.connect(self.worker_dataingestion.run)
        # connect buttons for general interface
        self.btn_back.clicked.connect(self.back_to_files)
        self.btn_apply_changes.clicked.connect(self.apply_changes)
        self.btn_refresh_plot.clicked.connect(self.apply_changes_plot_analysis)
        self.tab_widget.currentChanged.connect(self.toggle_results)
        self.signal_to_plot_analysis_results.connect(self.animation_widget.plot_analysis_results)
        self.signal_to_hide_analysis_results.connect(self.animation_widget.hide_analysis_results)
        # connect buttons that control animation playback
        self.btn_play.clicked.connect(self.play_animation)
        self.btn_pause.clicked.connect(self.pause_animation)
        self.btn_prev_frame.clicked.connect(self.pause_animation)
        self.btn_prev_frame.clicked.connect(self.show_processing_tab)
        self.btn_prev_frame.clicked.connect(self.animation_widget.show_previous_frame)
        self.btn_next_frame.clicked.connect(self.pause_animation)
        self.btn_next_frame.clicked.connect(self.show_processing_tab)
        self.btn_next_frame.clicked.connect(self.animation_widget.show_next_frame)
        self.btn_export.clicked.connect(self.export_plot)
        # tooltips
        children = self.findChildren(QLabelClickable)
        for child in children:
            child.clicked.connect(show_tooltip_on_click)

    def format_text_in_gui(self):
        # some of the text labels in the frontend require rich text formatting
        self.lbl_freq_separation.setText("Calc. freq. separation (<i>δf</i> ) (Hz)")
        self.lbl_k_spec.setText("K (# spectra to average)")
        self.lbl_t_int.setText("<i>τ</i><sub> int</sub> (seconds per FFT)")
        self.lbl_t_hop.setText("Sliding window step-size (<i>t</i><sub> hop </sub>)")
        self.lbl_graph_header.setStyleSheet('font-size: 20px; font: "Arial"; padding-top: 5px;')
        self.label_10.setText("ΔX Predicted (<i>δf</i><sub> calc</sub> )")
        self.label_17.setText("ΔX Observed (<i>δf</i><sub> obsv</sub> )")
        # ensure the title text on tab is visible, this fixes a bug where the text was white
        self.tab_widget.tabBar().setTabTextColor(0, QColor('black'))
        self.tab_widget.tabBar().setTabTextColor(1, QColor('black'))

    def setup_plotting_toolbar(self):

        # horizontal layout to add to main window
        hlayout = QtWidgets.QHBoxLayout()
        hlayout.setContentsMargins(0, 8, 0, 10)  # (left, top, right, bottom)

        # spacer items
        spacer1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                        QtWidgets.QSizePolicy.Minimum)
        spacer2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                        QtWidgets.QSizePolicy.Minimum)

        # create toolbar, passing canvas as first parameter, then parent
        toolbar = NavigationToolbar(self.animation_widget, self)
        toolbar.setMinimumSize(QtCore.QSize(600, 0))
        self.vlayout_right.insertWidget(2, toolbar)

        # add items in order
        hlayout.addItem(spacer1)
        hlayout.addWidget(toolbar)
        hlayout.addItem(spacer2)

        # add entire row to main window
        self.vlayout_right.insertLayout(2, hlayout)

        # adjust an adjacent widget to improve layout
        self.horizontalLayout_4.setContentsMargins(-1, 9, -1, 8)  # (left, top, right, bottom)

    @QtCore.pyqtSlot(object)
    def receive_data_from_worker(self, data_tuple):
        """ A method to receive products from data ingestion worker and setup animation widget. """

        # close the progress bar window
        self.progress_window.close()

        # unpack the tuple imported from the worker_dataingestion
        self.rcp_processed = data_tuple[0]
        self.lcp_processed = data_tuple[1]
        self.rcp_data = data_tuple[2]
        self.lcp_data = data_tuple[3]
        self.sample_rate = data_tuple[4]
        self.current_settings = data_tuple[5]

        # set the minimum and maximum limits for each user parameter
        self.set_min_and_max_limits()

        # show default parameters to user
        self.show_parameters(self.current_settings)

        # pass default parameters into animation widget, initialize plot
        self.setup_animation(self.current_settings, self.rcp_data, self.lcp_data)


class WorkerDataIngestion(QtCore.QObject):
    """ A class that functions as a worker, generating plots from a separate thread. """

    signal_to_return_data = QtCore.pyqtSignal(object)
    signal_progress = QtCore.pyqtSignal(int)

    def __init__(self, parent=None):
        # QtCore.QObject.__init__(self, parent=parent)
        super().__init__(parent)

    @QtCore.pyqtSlot(object, object, object)
    def run(self, rcp_file, lcp_file, userdefined_params):
        # show thread is running
        self.signal_progress.emit(10)

        # read data files into Numpy
        rcp_processed = file_to_numpy(rcp_file)
        self.signal_progress.emit(25)
        lcp_processed = file_to_numpy(lcp_file)
        self.signal_progress.emit(40)

        # isolate IQ data from processed file
        rcp_data = get_iq_data(rcp_processed, rcp_file.mission)
        self.signal_progress.emit(45)
        lcp_data = get_iq_data(lcp_processed, lcp_file.mission)
        self.signal_progress.emit(50)

        # get the sample rate of the data file
        sample_rate = get_sample_rate(rcp_processed, rcp_file.mission)
        self.signal_progress.emit(60)

        # if the user defend own acquisition geometry parameters for the dataset, use them
        if userdefined_params:
            dt_occ, radius_target, altitude_sc = userdefined_params
        else:
            dt_occ, radius_target, altitude_sc = None, None, None

        # get all parameters for radar analysis pipeline, using RCP file to set default values
        s = get_signal_processing_parameters(
            filenames=(rcp_file.file_name, lcp_file.file_name),
            rcp_data=rcp_data,
            lcp_data=lcp_data,
            sample_rate=sample_rate,
            band_name=rcp_file.band_name,
            global_time=rcp_file.start_time,
            mission=rcp_file.mission,
            dt_occ=dt_occ,
            radius_target=radius_target,
            altitude_sc=altitude_sc,
            file_start_time=rcp_file.start_time,
            file_end_time=rcp_file.stop_time,
            did_calculate_overview=False)

        # include a split second delay to show the user the progress has finished
        self.signal_progress.emit(95)
        time.sleep(0.20)
        self.signal_progress.emit(100)
        time.sleep(0.15)

        self.signal_to_return_data.emit((rcp_processed, lcp_processed, rcp_data, lcp_data,
                                         sample_rate, s))


class IngestionProgress(QDialog):
    def __init__(self, ctx, parent=None):
        super().__init__(parent)
        self.ctx = ctx
        self.initUI()
        self.show()

    def initUI(self):

        self.setMinimumWidth(450)
        # horizontal layout to add to main window
        vlayout = QtWidgets.QVBoxLayout()
        self.setLayout(vlayout)
        vlayout.setContentsMargins(5, 5, 5, 5)  # (left, top, right, bottom)

        # add the large PARSE graphic to be shown on the start window
        pixmap_parse_icon = QPixmap(QImage(self.ctx.img_custom_logo()))
        pixmap_parse_icon = pixmap_parse_icon.scaled(
            180, 180, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.label_parse_icon = QLabel()
        self.label_parse_icon.setPixmap(pixmap_parse_icon)
        self.label_parse_icon.setAlignment(Qt.AlignCenter)
        vlayout.addWidget(self.label_parse_icon)

        self.progress = QProgressBar(self)
        self.progress.setGeometry(0, 0, 300, 25)
        self.progress.setMaximum(100)
        self.progress.setTextVisible(False)
        vlayout.addWidget(self.progress)

        # set window properties
        self.setWindowTitle('Loading Data from Files...')
        self.setModal(True)
        screen_geometry = QGuiApplication.screens()[0].geometry()
        x = (screen_geometry.width() - self.width()) / 2
        y = ((screen_geometry.height() - self.height()) / 2) - (screen_geometry.height() * 0.05)
        self.move(x, y)

    @QtCore.pyqtSlot(int)
    def receive_progress(self, count):
        if count <= 10:
            self.setWindowTitle('Loading Data from Files... (1/2)')
        elif count <= 25:
            self.setWindowTitle('Loading Data from Files... (2/2)')
        elif count <= 40:
            self.setWindowTitle('Preparing Data... (1/2)')
        elif count <= 45:
            self.setWindowTitle('Preparing Data... (2/2)')
        elif count <= 50:
            self.setWindowTitle('Processing Data...')
        self.progress.setValue(count)


class ExportWindow(QMainWindow, ExportMenu_Ui):
    def __init__(self, ctx, rcp_x, rcp_y, lcp_x, lcp_y, fig, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ctx = ctx
        self.setupUi(self)

        # set the title
        self.setWindowTitle("Export Plot")

        # set text to be selectable
        set_text_selectable(self)

        # attributes
        self.rcp_x = rcp_x
        self.rcp_y = rcp_y
        self.lcp_x = lcp_x
        self.lcp_y = lcp_y
        self.fig = fig

        # connect UI elements using slots and signals
        self.btn_cancel.clicked.connect(self.cancel_export)
        self.btn_ascii.clicked.connect(self.export_as_ascii)
        self.btn_image.clicked.connect(self.export_as_image)

        self.centralwidget.setContentsMargins(10, 10, 10, 10)  # (left, top, right, bottom)
        self.verticalLayout_2.setSpacing(7)

        self.btn_ascii.setText("Export Plot as ASCII\n( TXT )")
        self.btn_image.setText("Export Plot as Image\n( PNG / PDF )")

        # center the window
        center_window(self)

    def cancel_export(self):
        self.close()

    def export_as_ascii(self):
        # export the current plot as a (.txt) file
        did_set_title = False
        rows = len(self.rcp_x)
        path = QFileDialog.getSaveFileName(self, 'Save File', os.getenv('HOME'),
                                           'Text files (*.txt)')
        if path[0] != '':
            with open(path[0], 'w') as file:
                for i in range(rows):
                    if not did_set_title:
                        file.write("X(Hz) RCP_Y(dB) LCP_Y(dB)\n")
                        did_set_title = True
                    file.write("{} {} {}\n".format(self.rcp_x[i], self.rcp_y[i], self.lcp_y[i]))
        self.close()

    def export_as_image(self):
        # export the current plot as an image file
        path = QFileDialog.getSaveFileName(self, 'Save File', os.getenv('HOME'),
                                           "Images (*.png *.pdf)")
        self.fig.savefig(path[0], dpi=300)
        self.close()


class QLabelClickable(QLabel):
    clicked = QtCore.pyqtSignal(str)

    def mousePressEvent(self, ev):
        self.clicked.emit(self.toolTip())


def center_window(main_window):
    # geometry of the main window
    qr = main_window.frameGeometry()
    # center point of screen
    cp = QDesktopWidget().availableGeometry().center()
    # move rectangle's center point to screen's center point
    qr.moveCenter(cp)
    # top left of rectangle becomes top left of window centering it
    main_window.move(qr.topLeft())

    # alternative technique that similarly does not work if a window's children force it to expand
    # qtRectangle = main_window.frameGeometry()
    # centerPoint = QDesktopWidget().availableGeometry().center()
    # qtRectangle.moveCenter(centerPoint)
    # main_window.move(qtRectangle.topLeft())


def set_text_selectable(window):
    # set spin boxes to ignore scroll events, so user doesn't change them accidentally
    opts = QtCore.Qt.FindChildrenRecursively
    labels = window.findChildren(QtWidgets.QLabel, options=opts)
    for box in labels:
        box.setTextInteractionFlags(Qt.TextSelectableByMouse)


def prevent_accidental_scroll_adjustments(window):
    # set spin boxes to ignore scroll events, so user doesn't change them accidentally
    opts = QtCore.Qt.FindChildrenRecursively
    spinboxes = window.findChildren(QtWidgets.QSpinBox, options=opts)
    doublespinboxes = window.findChildren(QtWidgets.QDoubleSpinBox, options=opts)
    datetimeedits = window.findChildren(QtWidgets.QDateTimeEdit, options=opts)
    timeedits = window.findChildren(QtWidgets.QTimeEdit, options=opts)
    for box in spinboxes:
        box.wheelEvent = lambda *event: None
    for box in doublespinboxes:
        box.wheelEvent = lambda *event: None
    for box in datetimeedits:
        box.wheelEvent = lambda *event: None
    for box in timeedits:
        box.wheelEvent = lambda *event: None


def show_tooltip_on_click(description):
    globalCursorPos = QCursor.pos()
    mouseScreen = qApp.desktop().screenNumber(globalCursorPos)
    mouseScreenGeometry = qApp.desktop().screen(mouseScreen).geometry()
    localCursorPos = globalCursorPos - mouseScreenGeometry.topLeft()
    QtWidgets.QToolTip.showText(localCursorPos, description)
