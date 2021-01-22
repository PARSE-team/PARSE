# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SignalAnalysis_v12.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1325, 833)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.centralwidget.setFont(font)
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
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btn_back.setFont(font)
        self.btn_back.setObjectName("btn_back")
        self.horizontalLayout_7.addWidget(self.btn_back)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem)
        self.vlayout_left.addLayout(self.horizontalLayout_7)
        self.group_aq_geometry = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.group_aq_geometry.setFont(font)
        self.group_aq_geometry.setObjectName("group_aq_geometry")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.group_aq_geometry)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.lbl_target = QtWidgets.QLabel(self.group_aq_geometry)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.lbl_target.setFont(font)
        self.lbl_target.setObjectName("lbl_target")
        self.gridLayout_3.addWidget(self.lbl_target, 0, 0, 1, 1)
        self.lbl_mission = QtWidgets.QLabel(self.group_aq_geometry)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.lbl_mission.setFont(font)
        self.lbl_mission.setObjectName("lbl_mission")
        self.gridLayout_3.addWidget(self.lbl_mission, 0, 1, 1, 1)
        self.combo_target = QtWidgets.QComboBox(self.group_aq_geometry)
        self.combo_target.setEnabled(True)
        self.combo_target.setEditable(True)
        self.combo_target.setObjectName("combo_target")
        self.gridLayout_3.addWidget(self.combo_target, 1, 0, 1, 1)
        self.combo_mission = QtWidgets.QComboBox(self.group_aq_geometry)
        self.combo_mission.setEnabled(True)
        self.combo_mission.setEditable(True)
        self.combo_mission.setObjectName("combo_mission")
        self.gridLayout_3.addWidget(self.combo_mission, 1, 1, 1, 1)
        self.lbl_occ_duration = QtWidgets.QLabel(self.group_aq_geometry)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.lbl_occ_duration.setFont(font)
        self.lbl_occ_duration.setObjectName("lbl_occ_duration")
        self.gridLayout_3.addWidget(self.lbl_occ_duration, 2, 0, 1, 1)
        self.lbl_eq_radius = QtWidgets.QLabel(self.group_aq_geometry)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.lbl_eq_radius.setFont(font)
        self.lbl_eq_radius.setObjectName("lbl_eq_radius")
        self.gridLayout_3.addWidget(self.lbl_eq_radius, 2, 1, 1, 1)
        self.spin_occ_duration = QtWidgets.QSpinBox(self.group_aq_geometry)
        self.spin_occ_duration.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.spin_occ_duration.setFont(font)
        self.spin_occ_duration.setMinimum(-100)
        self.spin_occ_duration.setProperty("value", 10)
        self.spin_occ_duration.setObjectName("spin_occ_duration")
        self.gridLayout_3.addWidget(self.spin_occ_duration, 3, 0, 1, 1)
        self.spin_eq_radius = QtWidgets.QSpinBox(self.group_aq_geometry)
        self.spin_eq_radius.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.spin_eq_radius.setFont(font)
        self.spin_eq_radius.setMinimum(-100)
        self.spin_eq_radius.setMaximum(1000000000)
        self.spin_eq_radius.setProperty("value", 286)
        self.spin_eq_radius.setObjectName("spin_eq_radius")
        self.gridLayout_3.addWidget(self.spin_eq_radius, 3, 1, 1, 1)
        self.lbl_sc_veolcity = QtWidgets.QLabel(self.group_aq_geometry)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.lbl_sc_veolcity.setFont(font)
        self.lbl_sc_veolcity.setObjectName("lbl_sc_veolcity")
        self.gridLayout_3.addWidget(self.lbl_sc_veolcity, 4, 0, 1, 1)
        self.lbl_lowest_alt = QtWidgets.QLabel(self.group_aq_geometry)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.lbl_lowest_alt.setFont(font)
        self.lbl_lowest_alt.setObjectName("lbl_lowest_alt")
        self.gridLayout_3.addWidget(self.lbl_lowest_alt, 4, 1, 1, 1)
        self.spin_sc_velocity = QtWidgets.QSpinBox(self.group_aq_geometry)
        self.spin_sc_velocity.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.spin_sc_velocity.setFont(font)
        self.spin_sc_velocity.setMinimum(-100)
        self.spin_sc_velocity.setMaximum(1000)
        self.spin_sc_velocity.setProperty("value", 200)
        self.spin_sc_velocity.setObjectName("spin_sc_velocity")
        self.gridLayout_3.addWidget(self.spin_sc_velocity, 5, 0, 1, 1)
        self.spin_lowest_alt = QtWidgets.QSpinBox(self.group_aq_geometry)
        self.spin_lowest_alt.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.spin_lowest_alt.setFont(font)
        self.spin_lowest_alt.setMinimum(-100)
        self.spin_lowest_alt.setMaximum(1000)
        self.spin_lowest_alt.setProperty("value", 210)
        self.spin_lowest_alt.setObjectName("spin_lowest_alt")
        self.gridLayout_3.addWidget(self.spin_lowest_alt, 5, 1, 1, 1)
        self.vlayout_left.addWidget(self.group_aq_geometry)
        self.group_radio_analysis = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.group_radio_analysis.setFont(font)
        self.group_radio_analysis.setObjectName("group_radio_analysis")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.group_radio_analysis)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.lbl_k_spec = QtWidgets.QLabel(self.group_radio_analysis)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.lbl_k_spec.setFont(font)
        self.lbl_k_spec.setObjectName("lbl_k_spec")
        self.gridLayout_4.addWidget(self.lbl_k_spec, 4, 0, 1, 1)
        self.lbl_l_win = QtWidgets.QLabel(self.group_radio_analysis)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.lbl_l_win.setFont(font)
        self.lbl_l_win.setObjectName("lbl_l_win")
        self.gridLayout_4.addWidget(self.lbl_l_win, 2, 0, 1, 1)
        self.spin_f_res = QtWidgets.QDoubleSpinBox(self.group_radio_analysis)
        self.spin_f_res.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.spin_f_res.setFont(font)
        self.spin_f_res.setDecimals(2)
        self.spin_f_res.setProperty("value", 0.39)
        self.spin_f_res.setObjectName("spin_f_res")
        self.gridLayout_4.addWidget(self.spin_f_res, 1, 1, 1, 1)
        self.lbl_f_res = QtWidgets.QLabel(self.group_radio_analysis)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.lbl_f_res.setFont(font)
        self.lbl_f_res.setObjectName("lbl_f_res")
        self.gridLayout_4.addWidget(self.lbl_f_res, 0, 1, 1, 1)
        self.lbl_delta_f = QtWidgets.QLabel(self.group_radio_analysis)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.lbl_delta_f.setFont(font)
        self.lbl_delta_f.setObjectName("lbl_delta_f")
        self.gridLayout_4.addWidget(self.lbl_delta_f, 0, 0, 1, 1)
        self.lbl_t_hop = QtWidgets.QLabel(self.group_radio_analysis)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.lbl_t_hop.setFont(font)
        self.lbl_t_hop.setObjectName("lbl_t_hop")
        self.gridLayout_4.addWidget(self.lbl_t_hop, 6, 0, 1, 1)
        self.lbl_timespan = QtWidgets.QLabel(self.group_radio_analysis)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.lbl_timespan.setFont(font)
        self.lbl_timespan.setObjectName("lbl_timespan")
        self.gridLayout_4.addWidget(self.lbl_timespan, 4, 1, 1, 1)
        self.lbl_thop_tint = QtWidgets.QLabel(self.group_radio_analysis)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.lbl_thop_tint.setFont(font)
        self.lbl_thop_tint.setObjectName("lbl_thop_tint")
        self.gridLayout_4.addWidget(self.lbl_thop_tint, 6, 1, 1, 1)
        self.double_t_hop = QtWidgets.QDoubleSpinBox(self.group_radio_analysis)
        self.double_t_hop.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.double_t_hop.setFont(font)
        self.double_t_hop.setProperty("value", 20.0)
        self.double_t_hop.setObjectName("double_t_hop")
        self.gridLayout_4.addWidget(self.double_t_hop, 7, 0, 1, 1)
        self.lbl_t_int = QtWidgets.QLabel(self.group_radio_analysis)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.lbl_t_int.setFont(font)
        self.lbl_t_int.setObjectName("lbl_t_int")
        self.gridLayout_4.addWidget(self.lbl_t_int, 2, 1, 1, 1)
        self.double_k_spec = QtWidgets.QDoubleSpinBox(self.group_radio_analysis)
        self.double_k_spec.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.double_k_spec.setFont(font)
        self.double_k_spec.setDecimals(2)
        self.double_k_spec.setProperty("value", 2.0)
        self.double_k_spec.setObjectName("double_k_spec")
        self.gridLayout_4.addWidget(self.double_k_spec, 5, 0, 1, 1)
        self.display_delta_f = QtWidgets.QSpinBox(self.group_radio_analysis)
        self.display_delta_f.setEnabled(False)
        self.display_delta_f.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.display_delta_f.setProperty("value", 12)
        self.display_delta_f.setObjectName("display_delta_f")
        self.gridLayout_4.addWidget(self.display_delta_f, 1, 0, 1, 1)
        self.display_l_win = QtWidgets.QSpinBox(self.group_radio_analysis)
        self.display_l_win.setEnabled(False)
        self.display_l_win.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.display_l_win.setMaximum(10000000)
        self.display_l_win.setProperty("value", 40960)
        self.display_l_win.setObjectName("display_l_win")
        self.gridLayout_4.addWidget(self.display_l_win, 3, 0, 1, 1)
        self.display_t_int = QtWidgets.QDoubleSpinBox(self.group_radio_analysis)
        self.display_t_int.setEnabled(False)
        self.display_t_int.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.display_t_int.setDecimals(2)
        self.display_t_int.setProperty("value", 2.5)
        self.display_t_int.setObjectName("display_t_int")
        self.gridLayout_4.addWidget(self.display_t_int, 3, 1, 1, 1)
        self.display_timespan = QtWidgets.QDoubleSpinBox(self.group_radio_analysis)
        self.display_timespan.setEnabled(False)
        self.display_timespan.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.display_timespan.setProperty("value", 5.0)
        self.display_timespan.setObjectName("display_timespan")
        self.gridLayout_4.addWidget(self.display_timespan, 5, 1, 1, 1)
        self.display_thop_tint = QtWidgets.QDoubleSpinBox(self.group_radio_analysis)
        self.display_thop_tint.setEnabled(False)
        self.display_thop_tint.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.display_thop_tint.setProperty("value", 1.0)
        self.display_thop_tint.setObjectName("display_thop_tint")
        self.gridLayout_4.addWidget(self.display_thop_tint, 7, 1, 1, 1)
        self.vlayout_left.addWidget(self.group_radio_analysis)
        self.group_wind_props = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.group_wind_props.setFont(font)
        self.group_wind_props.setObjectName("group_wind_props")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.group_wind_props)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.lbl_xmin = QtWidgets.QLabel(self.group_wind_props)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.lbl_xmin.setFont(font)
        self.lbl_xmin.setObjectName("lbl_xmin")
        self.gridLayout_5.addWidget(self.lbl_xmin, 0, 0, 1, 1)
        self.lbl_xmax = QtWidgets.QLabel(self.group_wind_props)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.lbl_xmax.setFont(font)
        self.lbl_xmax.setObjectName("lbl_xmax")
        self.gridLayout_5.addWidget(self.lbl_xmax, 0, 1, 1, 1)
        self.spin_xmin = QtWidgets.QSpinBox(self.group_wind_props)
        self.spin_xmin.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.spin_xmin.setFont(font)
        self.spin_xmin.setMinimum(-500)
        self.spin_xmin.setProperty("value", -300)
        self.spin_xmin.setObjectName("spin_xmin")
        self.gridLayout_5.addWidget(self.spin_xmin, 1, 0, 1, 1)
        self.spin_xmax = QtWidgets.QSpinBox(self.group_wind_props)
        self.spin_xmax.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.spin_xmax.setFont(font)
        self.spin_xmax.setMinimum(-50)
        self.spin_xmax.setMaximum(500)
        self.spin_xmax.setProperty("value", 300)
        self.spin_xmax.setObjectName("spin_xmax")
        self.gridLayout_5.addWidget(self.spin_xmax, 1, 1, 1, 1)
        self.lbl_ymin = QtWidgets.QLabel(self.group_wind_props)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.lbl_ymin.setFont(font)
        self.lbl_ymin.setObjectName("lbl_ymin")
        self.gridLayout_5.addWidget(self.lbl_ymin, 2, 0, 1, 1)
        self.lbl_ymax = QtWidgets.QLabel(self.group_wind_props)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.lbl_ymax.setFont(font)
        self.lbl_ymax.setObjectName("lbl_ymax")
        self.gridLayout_5.addWidget(self.lbl_ymax, 2, 1, 1, 1)
        self.spin_ymin = QtWidgets.QSpinBox(self.group_wind_props)
        self.spin_ymin.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.spin_ymin.setFont(font)
        self.spin_ymin.setMinimum(-100)
        self.spin_ymin.setMaximum(3)
        self.spin_ymin.setProperty("value", -10)
        self.spin_ymin.setObjectName("spin_ymin")
        self.gridLayout_5.addWidget(self.spin_ymin, 3, 0, 1, 1)
        self.spin_ymax = QtWidgets.QSpinBox(self.group_wind_props)
        self.spin_ymax.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.spin_ymax.setFont(font)
        self.spin_ymax.setMaximum(500)
        self.spin_ymax.setProperty("value", 50)
        self.spin_ymax.setObjectName("spin_ymax")
        self.gridLayout_5.addWidget(self.spin_ymax, 3, 1, 1, 1)
        self.vlayout_left.addWidget(self.group_wind_props)
        self.btn_run_animation = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.btn_run_animation.setFont(font)
        self.btn_run_animation.setObjectName("btn_run_animation")
        self.vlayout_left.addWidget(self.btn_run_animation)
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
        font.setFamily("Arial")
        font.setPointSize(18)
        self.lbl_graph_header.setFont(font)
        self.lbl_graph_header.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_graph_header.setObjectName("lbl_graph_header")
        self.vlayout_right.addWidget(self.lbl_graph_header)
        self.widget_animation = BSRAnimation(self.centralwidget)
        self.widget_animation.setObjectName("widget_animation")
        self.vlayout_right.addWidget(self.widget_animation)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
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
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.vlayout_right.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem3)
        self.btn_export = QtWidgets.QPushButton(self.centralwidget)
        self.btn_export.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.btn_export.setFont(font)
        self.btn_export.setObjectName("btn_export")
        self.horizontalLayout_5.addWidget(self.btn_export)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem4)
        self.vlayout_right.addLayout(self.horizontalLayout_5)
        self.horizontalLayout.addLayout(self.vlayout_right)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(2, 5)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1325, 26))
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
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_back.setText(_translate("MainWindow", "Back"))
        self.group_aq_geometry.setTitle(_translate("MainWindow", "Acquisition Geometry"))
        self.lbl_target.setText(_translate("MainWindow", "Target"))
        self.lbl_mission.setText(_translate("MainWindow", "Mission"))
        self.combo_target.setCurrentText(_translate("MainWindow", "Vesta"))
        self.combo_mission.setCurrentText(_translate("MainWindow", "Dawn"))
        self.lbl_occ_duration.setText(_translate("MainWindow", "Occultation Duration (min)"))
        self.lbl_eq_radius.setText(_translate("MainWindow", "Equatorial Radius (km)"))
        self.lbl_sc_veolcity.setText(_translate("MainWindow", "S/C Velocity (m/s)"))
        self.lbl_lowest_alt.setText(_translate("MainWindow", "Lowest Altitude (km)"))
        self.group_radio_analysis.setTitle(_translate("MainWindow", "Radio Data Analysis "))
        self.lbl_k_spec.setText(_translate("MainWindow", "K (# spectra per plot)"))
        self.lbl_l_win.setText(_translate("MainWindow", "L (# samples per FFT)"))
        self.lbl_f_res.setText(_translate("MainWindow", "Freq. resolution (Hz)"))
        self.lbl_delta_f.setText(_translate("MainWindow", "Calc. freq. separation (Hz)"))
        self.lbl_t_hop.setText(_translate("MainWindow", "Moving average overlap"))
        self.lbl_timespan.setText(_translate("MainWindow", "Timespan per plot (sec)"))
        self.lbl_thop_tint.setText(_translate("MainWindow", "t_hop (overlap in sec)"))
        self.double_t_hop.setSuffix(_translate("MainWindow", " %"))
        self.lbl_t_int.setText(_translate("MainWindow", "t-int (seconds per FFT)"))
        self.group_wind_props.setTitle(_translate("MainWindow", "Window Properties"))
        self.lbl_xmin.setText(_translate("MainWindow", "X-Axis min (Hz):"))
        self.lbl_xmax.setText(_translate("MainWindow", "X-Axis max (Hz):"))
        self.lbl_ymin.setText(_translate("MainWindow", "Y-Axis min (dB):"))
        self.lbl_ymax.setText(_translate("MainWindow", "Y-Axis max (dB)"))
        self.btn_run_animation.setText(_translate("MainWindow", "Run Animation"))
        self.lbl_graph_header.setText(_translate("MainWindow", "Output Power Spectra"))
        self.btn_play.setText(_translate("MainWindow", "Play"))
        self.btn_pause.setText(_translate("MainWindow", "Pause"))
        self.btn_export.setText(_translate("MainWindow", "Export..."))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionView.setText(_translate("MainWindow", "View"))

from animation import BSRAnimation
