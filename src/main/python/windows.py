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


from PyQt5.QtGui import QImage, QPixmap, QGuiApplication, QFont, QColor
from PyQt5.QtCore import Qt, QTime, QDate, QDateTime
from PyQt5.QtWidgets import QMainWindow, QAbstractItemView, QTableWidget, QTableWidgetItem, \
    QDialog, QProgressBar, QFileDialog, QLabel, QGridLayout, QWidget, QDesktopWidget

from ui.ui_20210204.StartScreen_v32 import Ui_MainWindow as Start_Ui
from ui.ui_20201106.FileSelection_v18_dawn import Ui_MainWindow as File_Ui_Standard
from ui.ui_20200906.FileSelection_v13 import Ui_MainWindow as File_Ui_DetachedLabel
from ui.ui_20210204.SignalAnalysis_v36 import Ui_MainWindow as Signal_Ui
# from ui.ui_20210131.ExportMenu_v1 import Ui_MainWindow as ExportMenu_Ui
from ui.ui_20210129.glucokeep_about import Ui_MainWindow as About_Ui

from read_data import find_polar_pair, file_to_numpy, get_iq_data, get_files, get_sample_rate, \
    strftime_DOY, strftime_hhmmss, strftime_yyyyDOYhhmmss, strftime_yyyyDOYhhmmssff, \
    strftime_yyyyDOY, strftime_timestamp, get_polar_compliment, convert_astropy_to_pyqt, \
    convert_pyqt_to_astropy
from signal_processing import get_signal_processing_parameters
from spectral_analysis import get_spectral_analysis_results
from astropy.time import Time, TimeDelta
import numpy as np
import time

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

        # connect signals and slots
        self.btn_dawnvesta.clicked.connect(self.choose_dawn)
        self.btn_rosetta.clicked.connect(self.choose_rosetta)
        # self.btn_userfile.clicked.connect(self.choose_userfile)
        self.btn_contact.clicked.connect(self.show_contact)
        self.btn_sourcecode.clicked.connect(self.show_sourcecode)

    def choose_dawn(self):
        self.file_window = FileWindowStandard(self.ctx, source='dawn')
        self.file_window.show()
        self.close()

    def choose_rosetta(self):
        self.file_window = FileWindowDetachedLabel(self.ctx, source='rosetta')
        self.file_window.show()
        self.close()

    def choose_userfile(self):
        # TODO: implement
        """self.userfile = QFileDialog.getOpenFileNames()
        print("chose file: " + str(self.userfile))
        if self.userfile:
            pass
            userfile = DataLabel(file_name='user-defined',
                                 label=None,
                                 path_to_label=None,
                                 path_to_data=self.userfile,
                                 mission='user-defined',
                                 band_name='user-defined',
                                 polarization='user-defined',
                                 start_time=None,
                                 stop_time=None)

            self.files_tuple = find_polar_pair(self.selected_file, self.data_labels)
            self.signal_window = SignalWindow(self.ctx, self.source, self.files_tuple)
            self.signal_window.show()
            self.close()
        else:
            # TODO: implement error dialog
            print("directory error")"""
        pass

    def show_contact(self):
        self.contact_window = ContactUsWindow(self.ctx)
        self.contact_window.show()
        self.close()

    def show_sourcecode(self):
        self.sourcecode_window = SourceCodeWindow(self.ctx)
        self.sourcecode_window.show()
        self.close()


class ContactUsWindow(QMainWindow, About_Ui):
    def __init__(self, ctx, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ctx = ctx
        self.setupUi(self)

        # set the title
        self.setWindowTitle("PARSE  Contact Us")

        # connect UI elements using slots and signals
        self.pushButton.clicked.connect(self.back_to_menu)

        self.label.setText("To contact the developer via email or GitHub,\n"
                           "please use the following links:")

        # provide link to email
        self.label_2.setOpenExternalLinks(True)
        self.label_2.setText(
            "<a href=paulsirri@gmail.com>paulsirri@gmail.com</a>")

        # provide link to GitHub
        self.label_3.setOpenExternalLinks(True)
        self.label_3.setText(
            "<a href=https://github.com/PARSE-team/PARSE>https://github.com/PARSE-team/PARSE</a>")

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
        self.setWindowTitle("PARSE  Source Code")

        # connect UI elements using slots and signals
        self.pushButton.clicked.connect(self.back_to_menu)

        self.label.setText("To view source code or learn more about PARSE,\n"
                           "please visit the project's official GitHub page:")

        # provide link to GitHub
        self.label_2.setOpenExternalLinks(True)
        self.label_2.setText(
            "<a href=https://github.com/PARSE-team/PARSE>https://github.com/PARSE-team/PARSE</a>")

        self.label_3.setText("")

    def back_to_menu(self):
        self.start_window = StartWindow(self.ctx)
        self.start_window.show()
        self.close()


class FileWindowDetachedLabel(QMainWindow, File_Ui_DetachedLabel):
    def __init__(self, ctx, source, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ctx = ctx
        self.setupUi(self)

        # set the title
        self.setWindowTitle("PARSE - File Selection")

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
        self.table_files.setFont(QFont("Monospace", 13))
        self.lbl_quickview.setFont(QFont("Monospace", 12))
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
    def __init__(self, ctx, source, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ctx = ctx
        self.setupUi(self)

        # set the title
        self.setWindowTitle("PARSE - File Selection")

        # set window size
        w = 800
        h = 600
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
        self.table_files.setFont(QFont("Monospace", 13))
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
        self.files_tuple = find_polar_pair(self.selected_file, self.data_labels)
        self.signal_window = SignalWindow(self.ctx, self.source, self.files_tuple)
        self.signal_window.show()
        self.close()


class SignalWindow(QMainWindow, Signal_Ui):
    signal_to_run_worker = QtCore.pyqtSignal(object, object)
    signal_to_plot_analysis_results = QtCore.pyqtSignal(object)
    signal_to_hide_analysis_results = QtCore.pyqtSignal()

    def __init__(self, ctx, source, files_tuple, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ctx = ctx
        self.setupUi(self)

        # set the title
        self.setWindowTitle("PARSE - Processing and Analysis")

        # set window size
        w = round(1920 * 0.80)
        h = round(1080 * 0.80)
        self.resize(w, h)

        # center the window
        center_window(self)

        # set the default active tab to "Signal Processing"
        self.tab_widget.setCurrentIndex(0)
        self.tab_widget.setTabEnabled(1, False)

        # set spin boxes to ignore scroll events, so user doesn't change them accidentally
        self.prevent_accidental_scroll_adjustments()

        self.tab_widget.setMinimumWidth(490)

        # format text labels in the interface
        self.format_text_in_gui()

        # create toolbar, passing canvas as first parameter, then parent
        toolbar = NavigationToolbar(self.animation_widget, self)
        self.vlayout_right.insertWidget(2, toolbar)

        # create a WorkerDataIngestion object and a thread
        self.worker_dataingestion = WorkerDataIngestion()
        self.worker_dataingestion_thread = QtCore.QThread()

        # assign the worker_dataingestion to the thread and start the thread
        self.worker_dataingestion.moveToThread(self.worker_dataingestion_thread)
        self.worker_dataingestion_thread.start()

        # dialog box to show worker progress
        self.progress_window = IngestionProgress(parent=self)
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
        self.signal_to_run_worker.emit(self.rcp_file, self.lcp_file)

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
        self.spin_bandwidth_global.setValue(msmt.bandwidth_RCP_at_max)
        self.spin_bandwidth_global_LCP.setValue(msmt.bandwidth_LCP_at_max)
        self.spin_noise_variance_global.setValue(msmt.Pxx_noise_var_RCP)
        self.spin_noise_variance_global_LCP.setValue(msmt.Pxx_noise_var_LCP)
        self.spin_delta_x_predict.setValue(msmt.df_calc)
        self.spin_delta_x_predict.setValue(msmt.df_calc)

        self.spin_ymax_local.setValue(msmt.Pxx_local_max_RCP)
        self.spin_ymax_local_LCP.setValue(msmt.Pxx_LCP_at_local_max)
        self.spin_x_at_ymax_local.setValue(msmt.freq_at_local_max)
        self.spin_bandwidth_local.setValue(msmt.bandwidth_RCP_local_max)
        self.spin_bandwidth_local_LCP.setValue(msmt.bandwidth_LCP_at_local_max)
        # self.spin_variance_local.setValue(msmt.Pxx_local_var)
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

        is_calculated = True
        if msmt.error_NdB_below:
            is_calculated = False
            self.show_error_message('Error: Bandwidth cannot be measured this far below peak.')
        if msmt.error_direct_signal:
            is_calculated = False
            self.show_error_message(
                'Warning: local max may not be a signal; '
                'detectability limit is >= 3 dB above the noise.')
        if msmt.error_finding_bandwidth:
            is_calculated = False
            self.show_error_message('Error: Unable to detect the bandwidth of the specified peak.')
        if is_calculated:
            self.signal_to_plot_analysis_results.emit(msmt)

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

            # provide error messages to help user diagnose issues
            is_calculated = True
            if self.msmt.error_NdB_below:
                is_calculated = False
                self.show_error_message('Error: Bandwidth cannot be measured this far below peak.')
            if self.msmt.error_direct_signal:
                is_calculated = False
                self.show_error_message(
                    'Warning: local max may not be a signal; '
                    'detectability limit is >= 3 dB above the noise.')
            if self.msmt.error_finding_bandwidth:
                is_calculated = False
                self.show_error_message(
                    'Error: Unable to detect the bandwidth of the specified peak.')
            if is_calculated:
                self.signal_to_plot_analysis_results.emit(self.msmt)
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

    def export_animation(self):
        # print('export attempted')
        pass

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
        """maximum_seconds = np.floor((self.rcp_file.stop_time
                                    - self.rcp_file.start_time).to_value('sec')
                                   - self.current_settings.seconds_for_welch)
        maximum_seconds = TimeDelta(maximum_seconds, format='sec')
        max_datetime = (self.rcp_file.start_time + maximum_seconds).strf('')"""
        pass

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
        self.btn_prev_frame.clicked.connect(self.animation_widget.show_previous_frame)
        self.btn_prev_frame.clicked.connect(self.pause_animation)
        self.btn_next_frame.clicked.connect(self.animation_widget.show_next_frame)
        self.btn_next_frame.clicked.connect(self.pause_animation)
        # todo: connect export button self.btn_export.clicked.connect(self.function)

    def prevent_accidental_scroll_adjustments(self):
        # set spin boxes to ignore scroll events, so user doesn't change them accidentally
        opts = QtCore.Qt.FindChildrenRecursively
        spinboxes = self.findChildren(QtWidgets.QSpinBox, options=opts)
        doublespinboxes = self.findChildren(QtWidgets.QDoubleSpinBox, options=opts)
        datetimeedits = self.findChildren(QtWidgets.QDateTimeEdit, options=opts)
        timeedits = self.findChildren(QtWidgets.QTimeEdit, options=opts)
        for box in spinboxes:
            box.wheelEvent = lambda *event: None
        for box in doublespinboxes:
            box.wheelEvent = lambda *event: None
        for box in datetimeedits:
            box.wheelEvent = lambda *event: None
        for box in timeedits:
            box.wheelEvent = lambda *event: None

    def format_text_in_gui(self):
        # some of the text labels in the frontend require rich text formatting
        self.lbl_freq_separation.setText("Calc. freq. separation (<i>δf</i> ) (Hz)")
        self.lbl_k_spec.setText("K (# spectra to average)")
        self.lbl_t_int.setText("<i>τ</i><sub> int</sub> (seconds per FFT)")
        self.lbl_t_hop.setText("Sliding window step-size (<i>t</i><sub> hop </sub>)")
        self.lbl_graph_header.setStyleSheet('font-size: 20px; font: "Arial"; padding-top: 5px;')
        # ensure the title text on tab is visible, this fixes a bug where the text was white
        self.tab_widget.tabBar().setTabTextColor(0, QColor('black'))
        self.tab_widget.tabBar().setTabTextColor(1, QColor('black'))

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

    @QtCore.pyqtSlot(object, object)
    def run(self, rcp_file, lcp_file):
        # read data files into Numpy
        rcp_processed = file_to_numpy(rcp_file)
        self.signal_progress.emit(10)
        lcp_processed = file_to_numpy(lcp_file)
        self.signal_progress.emit(20)

        # isolate IQ data from processed file
        rcp_data = get_iq_data(rcp_processed, rcp_file.mission)
        self.signal_progress.emit(40)

        lcp_data = get_iq_data(lcp_processed, lcp_file.mission)
        self.signal_progress.emit(60)

        # get the sample rate of the data file
        sample_rate = get_sample_rate(rcp_processed, rcp_file.mission)
        self.signal_progress.emit(70)

        # get all parameters for radar analysis pipeline, using RCP file to set default values
        s = get_signal_processing_parameters(
            filenames=(rcp_file.file_name, lcp_file.file_name),
            rcp_data=rcp_data,
            lcp_data=lcp_data,
            sample_rate=sample_rate,
            band_name=rcp_file.band_name,
            global_time=rcp_file.start_time,
            mission=rcp_file.mission,
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
    """
    Simple dialog that consists of a Progress Bar and a Button.
    Clicking on the button results in the start of a timer and
    updates the progress bar.
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()
        self.show()

    def initUI(self):
        self.setWindowTitle('Loading Data Files')
        self.progress = QProgressBar(self)
        self.progress.setGeometry(0, 0, 300, 25)
        self.progress.setMaximum(100)
        self.setModal(True)

        screen_geometry = QGuiApplication.screens()[0].geometry()
        x = (screen_geometry.width() - self.width()) / 2
        y = ((screen_geometry.height() - self.height()) / 2) - (screen_geometry.height() * 0.05)
        self.move(x, y)

    @QtCore.pyqtSlot(int)
    def receive_progress(self, count):
        self.progress.setValue(count)


def center_window(main_window):
    # center the window
    qtRectangle = main_window.frameGeometry()
    centerPoint = QDesktopWidget().availableGeometry().center()
    qtRectangle.moveCenter(centerPoint)
    main_window.move(qtRectangle.topLeft())
