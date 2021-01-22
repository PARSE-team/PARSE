# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SignalAnalysis_v15_tabs_v2.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1439, 817)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.vlayout_left = QtWidgets.QVBoxLayout()
        self.vlayout_left.setObjectName("vlayout_left")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.btn_back = QtWidgets.QPushButton(self.centralwidget)
        self.btn_back.setObjectName("btn_back")
        self.horizontalLayout_7.addWidget(self.btn_back)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem)
        self.vlayout_left.addLayout(self.horizontalLayout_7)
        self.tab_widget = QtWidgets.QTabWidget(self.centralwidget)
        self.tab_widget.setMinimumSize(QtCore.QSize(503, 0))
        self.tab_widget.setObjectName("tab_widget")
        self.tab_signal_animation = QtWidgets.QWidget()
        self.tab_signal_animation.setObjectName("tab_signal_animation")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.tab_signal_animation)
        self.gridLayout_6.setContentsMargins(-1, -1, -1, 21)
        self.gridLayout_6.setVerticalSpacing(17)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.btn_apply_changes = QtWidgets.QPushButton(self.tab_signal_animation)
        self.btn_apply_changes.setObjectName("btn_apply_changes")
        self.gridLayout_6.addWidget(self.btn_apply_changes, 1, 0, 1, 1)
        self.scrollArea = QtWidgets.QScrollArea(self.tab_signal_animation)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 452, 1070))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(-1, 10, -1, 22)
        self.verticalLayout.setSpacing(30)
        self.verticalLayout.setObjectName("verticalLayout")
        self.group_aq_geometry = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.group_aq_geometry.setAlignment(QtCore.Qt.AlignCenter)
        self.group_aq_geometry.setObjectName("group_aq_geometry")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.group_aq_geometry)
        self.gridLayout_3.setContentsMargins(-1, 16, -1, 16)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.lbl_lowest_alt = QtWidgets.QLabel(self.group_aq_geometry)
        self.lbl_lowest_alt.setObjectName("lbl_lowest_alt")
        self.gridLayout_3.addWidget(self.lbl_lowest_alt, 6, 1, 1, 1)
        self.lbl_sc_veolcity = QtWidgets.QLabel(self.group_aq_geometry)
        self.lbl_sc_veolcity.setObjectName("lbl_sc_veolcity")
        self.gridLayout_3.addWidget(self.lbl_sc_veolcity, 6, 0, 1, 1)
        self.spin_occ_duration = QtWidgets.QDoubleSpinBox(self.group_aq_geometry)
        self.spin_occ_duration.setDecimals(0)
        self.spin_occ_duration.setMaximum(1000.0)
        self.spin_occ_duration.setObjectName("spin_occ_duration")
        self.gridLayout_3.addWidget(self.spin_occ_duration, 4, 0, 1, 1)
        self.lbl_target = QtWidgets.QLabel(self.group_aq_geometry)
        self.lbl_target.setObjectName("lbl_target")
        self.gridLayout_3.addWidget(self.lbl_target, 0, 0, 1, 1)
        self.line_edit_mission = QtWidgets.QLineEdit(self.group_aq_geometry)
        self.line_edit_mission.setReadOnly(True)
        self.line_edit_mission.setObjectName("line_edit_mission")
        self.gridLayout_3.addWidget(self.line_edit_mission, 1, 1, 1, 1)
        self.spin_eq_radius = QtWidgets.QDoubleSpinBox(self.group_aq_geometry)
        self.spin_eq_radius.setDecimals(0)
        self.spin_eq_radius.setMaximum(100000.0)
        self.spin_eq_radius.setObjectName("spin_eq_radius")
        self.gridLayout_3.addWidget(self.spin_eq_radius, 4, 1, 1, 1)
        self.lbl_eq_radius = QtWidgets.QLabel(self.group_aq_geometry)
        self.lbl_eq_radius.setObjectName("lbl_eq_radius")
        self.gridLayout_3.addWidget(self.lbl_eq_radius, 3, 1, 1, 1)
        self.lbl_occ_duration = QtWidgets.QLabel(self.group_aq_geometry)
        self.lbl_occ_duration.setObjectName("lbl_occ_duration")
        self.gridLayout_3.addWidget(self.lbl_occ_duration, 3, 0, 1, 1)
        self.lbl_mission = QtWidgets.QLabel(self.group_aq_geometry)
        self.lbl_mission.setObjectName("lbl_mission")
        self.gridLayout_3.addWidget(self.lbl_mission, 0, 1, 1, 1)
        self.spin_lowest_alt = QtWidgets.QDoubleSpinBox(self.group_aq_geometry)
        self.spin_lowest_alt.setDecimals(0)
        self.spin_lowest_alt.setMaximum(10000.0)
        self.spin_lowest_alt.setObjectName("spin_lowest_alt")
        self.gridLayout_3.addWidget(self.spin_lowest_alt, 7, 1, 1, 1)
        self.line_edit_target = QtWidgets.QLineEdit(self.group_aq_geometry)
        self.line_edit_target.setReadOnly(True)
        self.line_edit_target.setObjectName("line_edit_target")
        self.gridLayout_3.addWidget(self.line_edit_target, 1, 0, 1, 1)
        self.spin_sc_velocity = QtWidgets.QDoubleSpinBox(self.group_aq_geometry)
        self.spin_sc_velocity.setDecimals(0)
        self.spin_sc_velocity.setMaximum(10000.0)
        self.spin_sc_velocity.setObjectName("spin_sc_velocity")
        self.gridLayout_3.addWidget(self.spin_sc_velocity, 7, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 7, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_3.addItem(spacerItem1, 2, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 7, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_3.addItem(spacerItem2, 5, 0, 1, 1)
        self.verticalLayout.addWidget(self.group_aq_geometry)
        self.group_radio_analysis = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.group_radio_analysis.setAlignment(QtCore.Qt.AlignCenter)
        self.group_radio_analysis.setObjectName("group_radio_analysis")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.group_radio_analysis)
        self.gridLayout_4.setContentsMargins(-1, 16, -1, 16)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.spin_l_win = QtWidgets.QDoubleSpinBox(self.group_radio_analysis)
        self.spin_l_win.setEnabled(False)
        self.spin_l_win.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.spin_l_win.setDecimals(0)
        self.spin_l_win.setMaximum(1000000.0)
        self.spin_l_win.setObjectName("spin_l_win")
        self.gridLayout_4.addWidget(self.spin_l_win, 4, 0, 1, 1)
        self.spin_t_int = QtWidgets.QDoubleSpinBox(self.group_radio_analysis)
        self.spin_t_int.setEnabled(False)
        self.spin_t_int.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.spin_t_int.setDecimals(2)
        self.spin_t_int.setMaximum(1000.0)
        self.spin_t_int.setObjectName("spin_t_int")
        self.gridLayout_4.addWidget(self.spin_t_int, 4, 1, 1, 1)
        self.spin_timespan = QtWidgets.QDoubleSpinBox(self.group_radio_analysis)
        self.spin_timespan.setEnabled(False)
        self.spin_timespan.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.spin_timespan.setMaximum(1000.0)
        self.spin_timespan.setObjectName("spin_timespan")
        self.gridLayout_4.addWidget(self.spin_timespan, 7, 1, 1, 1)
        self.spin_k_spec = QtWidgets.QDoubleSpinBox(self.group_radio_analysis)
        self.spin_k_spec.setEnabled(True)
        self.spin_k_spec.setDecimals(0)
        self.spin_k_spec.setMaximum(1000.0)
        self.spin_k_spec.setObjectName("spin_k_spec")
        self.gridLayout_4.addWidget(self.spin_k_spec, 7, 0, 1, 1)
        self.lbl_freq_res = QtWidgets.QLabel(self.group_radio_analysis)
        self.lbl_freq_res.setObjectName("lbl_freq_res")
        self.gridLayout_4.addWidget(self.lbl_freq_res, 0, 1, 1, 1)
        self.lbl_k_spec = QtWidgets.QLabel(self.group_radio_analysis)
        self.lbl_k_spec.setObjectName("lbl_k_spec")
        self.gridLayout_4.addWidget(self.lbl_k_spec, 6, 0, 1, 1)
        self.spin_freq_separation = QtWidgets.QDoubleSpinBox(self.group_radio_analysis)
        self.spin_freq_separation.setEnabled(False)
        self.spin_freq_separation.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.spin_freq_separation.setDecimals(0)
        self.spin_freq_separation.setMaximum(1000.0)
        self.spin_freq_separation.setObjectName("spin_freq_separation")
        self.gridLayout_4.addWidget(self.spin_freq_separation, 1, 0, 1, 1)
        self.lbl_t_hop = QtWidgets.QLabel(self.group_radio_analysis)
        self.lbl_t_hop.setObjectName("lbl_t_hop")
        self.gridLayout_4.addWidget(self.lbl_t_hop, 9, 1, 1, 1)
        self.spin_t_hop = QtWidgets.QDoubleSpinBox(self.group_radio_analysis)
        self.spin_t_hop.setEnabled(False)
        self.spin_t_hop.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.spin_t_hop.setMaximum(1000.0)
        self.spin_t_hop.setObjectName("spin_t_hop")
        self.gridLayout_4.addWidget(self.spin_t_hop, 10, 1, 1, 1)
        self.lbl_l_win = QtWidgets.QLabel(self.group_radio_analysis)
        self.lbl_l_win.setObjectName("lbl_l_win")
        self.gridLayout_4.addWidget(self.lbl_l_win, 3, 0, 1, 1)
        self.lbl_t_int = QtWidgets.QLabel(self.group_radio_analysis)
        self.lbl_t_int.setObjectName("lbl_t_int")
        self.gridLayout_4.addWidget(self.lbl_t_int, 3, 1, 1, 1)
        self.spin_freq_res = QtWidgets.QDoubleSpinBox(self.group_radio_analysis)
        self.spin_freq_res.setEnabled(True)
        self.spin_freq_res.setDecimals(2)
        self.spin_freq_res.setMaximum(1000.0)
        self.spin_freq_res.setSingleStep(0.01)
        self.spin_freq_res.setObjectName("spin_freq_res")
        self.gridLayout_4.addWidget(self.spin_freq_res, 1, 1, 1, 1)
        self.lbl_freq_separation = QtWidgets.QLabel(self.group_radio_analysis)
        self.lbl_freq_separation.setObjectName("lbl_freq_separation")
        self.gridLayout_4.addWidget(self.lbl_freq_separation, 0, 0, 1, 1)
        self.lbl_timespan = QtWidgets.QLabel(self.group_radio_analysis)
        self.lbl_timespan.setObjectName("lbl_timespan")
        self.gridLayout_4.addWidget(self.lbl_timespan, 6, 1, 1, 1)
        self.lbl_moving_overlap = QtWidgets.QLabel(self.group_radio_analysis)
        self.lbl_moving_overlap.setObjectName("lbl_moving_overlap")
        self.gridLayout_4.addWidget(self.lbl_moving_overlap, 9, 0, 1, 1)
        self.spin_moving_overlap = QtWidgets.QDoubleSpinBox(self.group_radio_analysis)
        self.spin_moving_overlap.setEnabled(True)
        self.spin_moving_overlap.setDecimals(0)
        self.spin_moving_overlap.setObjectName("spin_moving_overlap")
        self.gridLayout_4.addWidget(self.spin_moving_overlap, 10, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 7, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_4.addItem(spacerItem3, 2, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 7, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_4.addItem(spacerItem4, 5, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 7, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_4.addItem(spacerItem5, 8, 0, 1, 1)
        self.verticalLayout.addWidget(self.group_radio_analysis)
        self.group_wind_props = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.group_wind_props.setAlignment(QtCore.Qt.AlignCenter)
        self.group_wind_props.setObjectName("group_wind_props")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.group_wind_props)
        self.gridLayout_5.setContentsMargins(-1, 16, -1, 16)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.lbl_xmax = QtWidgets.QLabel(self.group_wind_props)
        self.lbl_xmax.setObjectName("lbl_xmax")
        self.gridLayout_5.addWidget(self.lbl_xmax, 0, 1, 1, 1)
        self.spin_ymax = QtWidgets.QDoubleSpinBox(self.group_wind_props)
        self.spin_ymax.setDecimals(0)
        self.spin_ymax.setMinimum(-1000.0)
        self.spin_ymax.setMaximum(1000.0)
        self.spin_ymax.setObjectName("spin_ymax")
        self.gridLayout_5.addWidget(self.spin_ymax, 4, 1, 1, 1)
        self.lbl_ymax = QtWidgets.QLabel(self.group_wind_props)
        self.lbl_ymax.setObjectName("lbl_ymax")
        self.gridLayout_5.addWidget(self.lbl_ymax, 3, 1, 1, 1)
        self.spin_ymin = QtWidgets.QDoubleSpinBox(self.group_wind_props)
        self.spin_ymin.setDecimals(0)
        self.spin_ymin.setMinimum(-1000.0)
        self.spin_ymin.setMaximum(1000.0)
        self.spin_ymin.setObjectName("spin_ymin")
        self.gridLayout_5.addWidget(self.spin_ymin, 4, 0, 1, 1)
        self.lbl_xmin = QtWidgets.QLabel(self.group_wind_props)
        self.lbl_xmin.setObjectName("lbl_xmin")
        self.gridLayout_5.addWidget(self.lbl_xmin, 0, 0, 1, 1)
        self.spin_xmax = QtWidgets.QDoubleSpinBox(self.group_wind_props)
        self.spin_xmax.setDecimals(0)
        self.spin_xmax.setMinimum(-10000.0)
        self.spin_xmax.setMaximum(10000.0)
        self.spin_xmax.setObjectName("spin_xmax")
        self.gridLayout_5.addWidget(self.spin_xmax, 1, 1, 1, 1)
        self.lbl_ymin = QtWidgets.QLabel(self.group_wind_props)
        self.lbl_ymin.setObjectName("lbl_ymin")
        self.gridLayout_5.addWidget(self.lbl_ymin, 3, 0, 1, 1)
        self.spin_xmin = QtWidgets.QDoubleSpinBox(self.group_wind_props)
        self.spin_xmin.setDecimals(0)
        self.spin_xmin.setMinimum(-10000.0)
        self.spin_xmin.setMaximum(10000.0)
        self.spin_xmin.setObjectName("spin_xmin")
        self.gridLayout_5.addWidget(self.spin_xmin, 1, 0, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 7, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_5.addItem(spacerItem6, 2, 0, 1, 1)
        self.verticalLayout.addWidget(self.group_wind_props)
        self.group_ani_playback = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.group_ani_playback.setAlignment(QtCore.Qt.AlignCenter)
        self.group_ani_playback.setObjectName("group_ani_playback")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.group_ani_playback)
        self.gridLayout_2.setContentsMargins(-1, 16, -1, 16)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lbl_start_sec = QtWidgets.QLabel(self.group_ani_playback)
        self.lbl_start_sec.setObjectName("lbl_start_sec")
        self.gridLayout_2.addWidget(self.lbl_start_sec, 0, 0, 1, 1)
        self.spin_start_sec = QtWidgets.QDoubleSpinBox(self.group_ani_playback)
        self.spin_start_sec.setDecimals(0)
        self.spin_start_sec.setObjectName("spin_start_sec")
        self.gridLayout_2.addWidget(self.spin_start_sec, 1, 0, 1, 1)
        self.lbl_ani_speed = QtWidgets.QLabel(self.group_ani_playback)
        self.lbl_ani_speed.setObjectName("lbl_ani_speed")
        self.gridLayout_2.addWidget(self.lbl_ani_speed, 0, 1, 1, 1)
        self.spin_ani_speed = QtWidgets.QDoubleSpinBox(self.group_ani_playback)
        self.spin_ani_speed.setDecimals(2)
        self.spin_ani_speed.setMaximum(10.0)
        self.spin_ani_speed.setObjectName("spin_ani_speed")
        self.gridLayout_2.addWidget(self.spin_ani_speed, 1, 1, 1, 1)
        self.verticalLayout.addWidget(self.group_ani_playback)
        spacerItem7 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem7)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_6.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.tab_widget.addTab(self.tab_signal_animation, "")
        self.tab_analysis = QtWidgets.QWidget()
        self.tab_analysis.setObjectName("tab_analysis")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.tab_analysis)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.tab_analysis)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 452, 837))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setContentsMargins(-1, 10, -1, 22)
        self.verticalLayout_4.setSpacing(30)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.group_settings = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_2)
        self.group_settings.setAlignment(QtCore.Qt.AlignCenter)
        self.group_settings.setObjectName("group_settings")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.group_settings)
        self.gridLayout_8.setContentsMargins(-1, 16, -1, 16)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.group_settings)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.spin_measure_bandwidth_below = QtWidgets.QDoubleSpinBox(self.group_settings)
        self.spin_measure_bandwidth_below.setDecimals(0)
        self.spin_measure_bandwidth_below.setMaximum(1000.0)
        self.spin_measure_bandwidth_below.setObjectName("spin_measure_bandwidth_below")
        self.horizontalLayout_2.addWidget(self.spin_measure_bandwidth_below)
        self.label_2 = QtWidgets.QLabel(self.group_settings)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        spacerItem8 = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem8)
        self.label_3 = QtWidgets.QLabel(self.group_settings)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.gridLayout_10 = QtWidgets.QGridLayout()
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.spin_x_min = QtWidgets.QDoubleSpinBox(self.group_settings)
        self.spin_x_min.setDecimals(0)
        self.spin_x_min.setMinimum(-10000.0)
        self.spin_x_min.setMaximum(10000.0)
        self.spin_x_min.setObjectName("spin_x_min")
        self.gridLayout_10.addWidget(self.spin_x_min, 1, 0, 1, 1)
        self.spin_x_max = QtWidgets.QDoubleSpinBox(self.group_settings)
        self.spin_x_max.setDecimals(0)
        self.spin_x_max.setMinimum(-10000.0)
        self.spin_x_max.setMaximum(10000.0)
        self.spin_x_max.setObjectName("spin_x_max")
        self.gridLayout_10.addWidget(self.spin_x_max, 1, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.group_settings)
        self.label_4.setObjectName("label_4")
        self.gridLayout_10.addWidget(self.label_4, 0, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.group_settings)
        self.label_5.setObjectName("label_5")
        self.gridLayout_10.addWidget(self.label_5, 0, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_10)
        spacerItem9 = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem9)
        self.pushButton = QtWidgets.QPushButton(self.group_settings)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton)
        self.gridLayout_8.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.verticalLayout_4.addWidget(self.group_settings)
        self.group_results = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_2)
        self.group_results.setAlignment(QtCore.Qt.AlignCenter)
        self.group_results.setObjectName("group_results")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.group_results)
        self.gridLayout_12.setContentsMargins(-1, 16, -1, 16)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.gridLayout_11 = QtWidgets.QGridLayout()
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.label_10 = QtWidgets.QLabel(self.group_results)
        self.label_10.setObjectName("label_10")
        self.gridLayout_11.addWidget(self.label_10, 4, 0, 1, 1)
        self.spin_bandwidth_global = QtWidgets.QDoubleSpinBox(self.group_results)
        self.spin_bandwidth_global.setDecimals(0)
        self.spin_bandwidth_global.setMinimum(-1000.0)
        self.spin_bandwidth_global.setMaximum(1000.0)
        self.spin_bandwidth_global.setObjectName("spin_bandwidth_global")
        self.gridLayout_11.addWidget(self.spin_bandwidth_global, 2, 1, 1, 1)
        self.spin_ymax_global = QtWidgets.QDoubleSpinBox(self.group_results)
        self.spin_ymax_global.setDecimals(0)
        self.spin_ymax_global.setMinimum(-1000.0)
        self.spin_ymax_global.setMaximum(1000.0)
        self.spin_ymax_global.setObjectName("spin_ymax_global")
        self.gridLayout_11.addWidget(self.spin_ymax_global, 0, 1, 1, 1)
        self.spin_ymax_local = QtWidgets.QDoubleSpinBox(self.group_results)
        self.spin_ymax_local.setDecimals(0)
        self.spin_ymax_local.setMinimum(-1000.0)
        self.spin_ymax_local.setMaximum(1000.0)
        self.spin_ymax_local.setObjectName("spin_ymax_local")
        self.gridLayout_11.addWidget(self.spin_ymax_local, 7, 1, 1, 1)
        self.spin_noise_variance_global = QtWidgets.QDoubleSpinBox(self.group_results)
        self.spin_noise_variance_global.setDecimals(0)
        self.spin_noise_variance_global.setMinimum(-1000.0)
        self.spin_noise_variance_global.setMaximum(1000.0)
        self.spin_noise_variance_global.setObjectName("spin_noise_variance_global")
        self.gridLayout_11.addWidget(self.spin_noise_variance_global, 3, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.group_results)
        self.label_12.setObjectName("label_12")
        self.gridLayout_11.addWidget(self.label_12, 7, 0, 1, 1)
        self.spin_delta_x_predict = QtWidgets.QDoubleSpinBox(self.group_results)
        self.spin_delta_x_predict.setDecimals(0)
        self.spin_delta_x_predict.setMinimum(0.0)
        self.spin_delta_x_predict.setMaximum(1000.0)
        self.spin_delta_x_predict.setObjectName("spin_delta_x_predict")
        self.gridLayout_11.addWidget(self.spin_delta_x_predict, 4, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.group_results)
        self.label_6.setObjectName("label_6")
        self.gridLayout_11.addWidget(self.label_6, 0, 0, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.group_results)
        self.label_14.setObjectName("label_14")
        self.gridLayout_11.addWidget(self.label_14, 9, 0, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.group_results)
        self.label_15.setObjectName("label_15")
        self.gridLayout_11.addWidget(self.label_15, 10, 0, 1, 1)
        self.spin_delta_x_observed = QtWidgets.QDoubleSpinBox(self.group_results)
        self.spin_delta_x_observed.setDecimals(0)
        self.spin_delta_x_observed.setMinimum(-1000.0)
        self.spin_delta_x_observed.setMaximum(1000.0)
        self.spin_delta_x_observed.setObjectName("spin_delta_x_observed")
        self.gridLayout_11.addWidget(self.spin_delta_x_observed, 12, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.group_results)
        self.label_8.setObjectName("label_8")
        self.gridLayout_11.addWidget(self.label_8, 2, 0, 1, 1)
        self.spin_delta_y = QtWidgets.QDoubleSpinBox(self.group_results)
        self.spin_delta_y.setDecimals(0)
        self.spin_delta_y.setMinimum(-1000.0)
        self.spin_delta_y.setMaximum(1000.0)
        self.spin_delta_y.setObjectName("spin_delta_y")
        self.gridLayout_11.addWidget(self.spin_delta_y, 11, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.group_results)
        self.label_7.setObjectName("label_7")
        self.gridLayout_11.addWidget(self.label_7, 1, 0, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.group_results)
        self.label_13.setObjectName("label_13")
        self.gridLayout_11.addWidget(self.label_13, 8, 0, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.group_results)
        self.label_16.setObjectName("label_16")
        self.gridLayout_11.addWidget(self.label_16, 11, 0, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.group_results)
        self.label_17.setObjectName("label_17")
        self.gridLayout_11.addWidget(self.label_17, 12, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.group_results)
        self.label_9.setObjectName("label_9")
        self.gridLayout_11.addWidget(self.label_9, 3, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.group_results)
        self.label_11.setObjectName("label_11")
        self.gridLayout_11.addWidget(self.label_11, 6, 0, 1, 1)
        self.spin_x_at_ymax_global = QtWidgets.QDoubleSpinBox(self.group_results)
        self.spin_x_at_ymax_global.setDecimals(0)
        self.spin_x_at_ymax_global.setMinimum(-1000.0)
        self.spin_x_at_ymax_global.setMaximum(1000.0)
        self.spin_x_at_ymax_global.setObjectName("spin_x_at_ymax_global")
        self.gridLayout_11.addWidget(self.spin_x_at_ymax_global, 1, 1, 1, 1)
        self.spin_bandwidth_local = QtWidgets.QDoubleSpinBox(self.group_results)
        self.spin_bandwidth_local.setDecimals(0)
        self.spin_bandwidth_local.setMinimum(-1000.0)
        self.spin_bandwidth_local.setMaximum(1000.0)
        self.spin_bandwidth_local.setObjectName("spin_bandwidth_local")
        self.gridLayout_11.addWidget(self.spin_bandwidth_local, 9, 1, 1, 1)
        self.spin_variance_local = QtWidgets.QDoubleSpinBox(self.group_results)
        self.spin_variance_local.setDecimals(0)
        self.spin_variance_local.setMinimum(-1000.0)
        self.spin_variance_local.setMaximum(1000.0)
        self.spin_variance_local.setObjectName("spin_variance_local")
        self.gridLayout_11.addWidget(self.spin_variance_local, 10, 1, 1, 1)
        self.spin_x_at_ymax_local = QtWidgets.QDoubleSpinBox(self.group_results)
        self.spin_x_at_ymax_local.setDecimals(0)
        self.spin_x_at_ymax_local.setMinimum(-1000.0)
        self.spin_x_at_ymax_local.setMaximum(1000.0)
        self.spin_x_at_ymax_local.setObjectName("spin_x_at_ymax_local")
        self.gridLayout_11.addWidget(self.spin_x_at_ymax_local, 8, 1, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_11.addItem(spacerItem10, 5, 0, 1, 1)
        self.gridLayout_12.addLayout(self.gridLayout_11, 0, 0, 1, 1)
        self.verticalLayout_4.addWidget(self.group_results)
        spacerItem11 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem11)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.gridLayout_7.addWidget(self.scrollArea_2, 0, 0, 1, 1)
        self.tab_widget.addTab(self.tab_analysis, "")
        self.vlayout_left.addWidget(self.tab_widget)
        self.horizontalLayout.addLayout(self.vlayout_left)
        self.vline_center_divider = QtWidgets.QFrame(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.vline_center_divider.setFont(font)
        self.vline_center_divider.setFrameShape(QtWidgets.QFrame.VLine)
        self.vline_center_divider.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.vline_center_divider.setObjectName("vline_center_divider")
        self.horizontalLayout.addWidget(self.vline_center_divider)
        self.vlayout_right = QtWidgets.QVBoxLayout()
        self.vlayout_right.setObjectName("vlayout_right")
        self.lbl_graph_header = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.lbl_graph_header.setFont(font)
        self.lbl_graph_header.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_graph_header.setObjectName("lbl_graph_header")
        self.vlayout_right.addWidget(self.lbl_graph_header)
        self.animation_widget = BSRAnimation(self.centralwidget)
        self.animation_widget.setObjectName("animation_widget")
        self.vlayout_right.addWidget(self.animation_widget)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem12)
        self.btn_prev_frame = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btn_prev_frame.setFont(font)
        self.btn_prev_frame.setObjectName("btn_prev_frame")
        self.horizontalLayout_3.addWidget(self.btn_prev_frame)
        self.btn_play = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btn_play.setFont(font)
        self.btn_play.setObjectName("btn_play")
        self.horizontalLayout_3.addWidget(self.btn_play)
        self.btn_pause = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btn_pause.setFont(font)
        self.btn_pause.setObjectName("btn_pause")
        self.horizontalLayout_3.addWidget(self.btn_pause)
        self.btn_next_frame = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btn_next_frame.setFont(font)
        self.btn_next_frame.setObjectName("btn_next_frame")
        self.horizontalLayout_3.addWidget(self.btn_next_frame)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem13)
        self.vlayout_right.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem14)
        self.btn_export = QtWidgets.QPushButton(self.centralwidget)
        self.btn_export.setEnabled(True)
        self.btn_export.setObjectName("btn_export")
        self.horizontalLayout_5.addWidget(self.btn_export)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem15)
        self.vlayout_right.addLayout(self.horizontalLayout_5)
        self.horizontalLayout.addLayout(self.vlayout_right)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(2, 5)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1439, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.menuHelp.setFont(font)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.actionView = QtWidgets.QAction(MainWindow)
        self.actionView.setObjectName("actionView")
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.tab_widget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.btn_back.setText(_translate("MainWindow", "Back"))
        self.btn_apply_changes.setText(_translate("MainWindow", "Apply Changes"))
        self.group_aq_geometry.setTitle(_translate("MainWindow", "Acquisition Geometry"))
        self.lbl_lowest_alt.setText(_translate("MainWindow", "Lowest Altitude (km)"))
        self.lbl_sc_veolcity.setText(_translate("MainWindow", "S/C Velocity (m/s)"))
        self.lbl_target.setText(_translate("MainWindow", "Target"))
        self.lbl_eq_radius.setText(_translate("MainWindow", "Equatorial Radius (km)"))
        self.lbl_occ_duration.setText(_translate("MainWindow", "Occultation Duration (min)"))
        self.lbl_mission.setText(_translate("MainWindow", "Mission"))
        self.group_radio_analysis.setTitle(_translate("MainWindow", "Radio Data Analysis "))
        self.lbl_freq_res.setText(_translate("MainWindow", "Freq. resolution (Hz)"))
        self.lbl_k_spec.setText(_translate("MainWindow", "K (# spectra per plot)"))
        self.lbl_t_hop.setText(_translate("MainWindow", "t_hop (overlap in sec)"))
        self.lbl_l_win.setText(_translate("MainWindow", "L (# samples per FFT)"))
        self.lbl_t_int.setText(_translate("MainWindow", "t-int (seconds per FFT)"))
        self.lbl_freq_separation.setText(_translate("MainWindow", "Calc. freq. separation (Hz)"))
        self.lbl_timespan.setText(_translate("MainWindow", "Timespan per plot (sec)"))
        self.lbl_moving_overlap.setText(_translate("MainWindow", "Moving average overlap"))
        self.spin_moving_overlap.setSuffix(_translate("MainWindow", " %"))
        self.group_wind_props.setTitle(_translate("MainWindow", "Window Properties"))
        self.lbl_xmax.setText(_translate("MainWindow", "X-Axis max (Hz):"))
        self.lbl_ymax.setText(_translate("MainWindow", "Y-Axis max (dB)"))
        self.lbl_xmin.setText(_translate("MainWindow", "X-Axis min (Hz):"))
        self.lbl_ymin.setText(_translate("MainWindow", "Y-Axis min (dB):"))
        self.group_ani_playback.setTitle(_translate("MainWindow", "Animation Playback"))
        self.lbl_start_sec.setText(_translate("MainWindow", "Start Second in File"))
        self.lbl_ani_speed.setText(_translate("MainWindow", "Animation Speed (fps)"))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab_signal_animation), _translate("MainWindow", "Signal Processing"))
        self.group_settings.setTitle(_translate("MainWindow", "Settings"))
        self.label.setText(_translate("MainWindow", "Measure bandwidths at"))
        self.spin_measure_bandwidth_below.setSuffix(_translate("MainWindow", " dB"))
        self.label_2.setText(_translate("MainWindow", "below peaks"))
        self.label_3.setText(_translate("MainWindow", "Find local maximum between:"))
        self.label_4.setText(_translate("MainWindow", "X-Axis min (Hz)"))
        self.label_5.setText(_translate("MainWindow", "X-Axis max (Hz)"))
        self.pushButton.setText(_translate("MainWindow", "Refresh Plot"))
        self.group_results.setTitle(_translate("MainWindow", "Results"))
        self.label_10.setText(_translate("MainWindow", "∆X Predicted (ẟf):"))
        self.spin_bandwidth_global.setSuffix(_translate("MainWindow", " Hz"))
        self.spin_ymax_global.setSuffix(_translate("MainWindow", " dB"))
        self.spin_ymax_local.setSuffix(_translate("MainWindow", " dB"))
        self.spin_noise_variance_global.setSuffix(_translate("MainWindow", " dB"))
        self.label_12.setText(_translate("MainWindow", "Y-Max (local):"))
        self.spin_delta_x_predict.setPrefix(_translate("MainWindow", "± "))
        self.spin_delta_x_predict.setSuffix(_translate("MainWindow", " Hz"))
        self.label_6.setText(_translate("MainWindow", "Y-Max (global):"))
        self.label_14.setText(_translate("MainWindow", "Bandwidth:"))
        self.label_15.setText(_translate("MainWindow", "Variance:"))
        self.spin_delta_x_observed.setSuffix(_translate("MainWindow", " Hz"))
        self.label_8.setText(_translate("MainWindow", "Bandwidth:"))
        self.spin_delta_y.setSuffix(_translate("MainWindow", " dB"))
        self.label_7.setText(_translate("MainWindow", "X at Y-Max:"))
        self.label_13.setText(_translate("MainWindow", "X at Y-Max:"))
        self.label_16.setText(_translate("MainWindow", "∆Y-Max:"))
        self.label_17.setText(_translate("MainWindow", "∆X Observed (ẟf):"))
        self.label_9.setText(_translate("MainWindow", "Noise Variance:"))
        self.label_11.setText(_translate("MainWindow", "Selected Range:"))
        self.spin_x_at_ymax_global.setSuffix(_translate("MainWindow", " Hz"))
        self.spin_bandwidth_local.setSuffix(_translate("MainWindow", " Hz"))
        self.spin_variance_local.setSuffix(_translate("MainWindow", " dB"))
        self.spin_x_at_ymax_local.setSuffix(_translate("MainWindow", " Hz"))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab_analysis), _translate("MainWindow", "Power Spectral Analysis"))
        self.lbl_graph_header.setText(_translate("MainWindow", "Output Power Spectra"))
        self.btn_prev_frame.setText(_translate("MainWindow", "<  Skip Frame"))
        self.btn_play.setText(_translate("MainWindow", "Play"))
        self.btn_pause.setText(_translate("MainWindow", "Pause"))
        self.btn_next_frame.setText(_translate("MainWindow", "Skip Frame  >"))
        self.btn_export.setText(_translate("MainWindow", "Export..."))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionView.setText(_translate("MainWindow", "View"))

from animation import BSRAnimation
