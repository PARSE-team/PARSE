# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FileSelection_Standard_v20.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1341, 838)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setContentsMargins(25, 15, 25, 5)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(-1, -1, -1, 10)
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btn_back = QtWidgets.QPushButton(self.centralwidget)
        self.btn_back.setObjectName("btn_back")
        self.horizontalLayout_2.addWidget(self.btn_back)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.hlayout_title = QtWidgets.QHBoxLayout()
        self.hlayout_title.setObjectName("hlayout_title")
        self.lbl_instructions = QtWidgets.QLabel(self.centralwidget)
        self.lbl_instructions.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_instructions.setObjectName("lbl_instructions")
        self.hlayout_title.addWidget(self.lbl_instructions)
        self.hlayout_title.setStretch(0, 1)
        self.verticalLayout.addLayout(self.hlayout_title)
        self.hlayout_content = QtWidgets.QHBoxLayout()
        self.hlayout_content.setSpacing(15)
        self.hlayout_content.setObjectName("hlayout_content")
        self.table_files = QtWidgets.QTableWidget(self.centralwidget)
        self.table_files.setObjectName("table_files")
        self.table_files.setColumnCount(0)
        self.table_files.setRowCount(0)
        self.hlayout_content.addWidget(self.table_files)
        self.verticalLayout.addLayout(self.hlayout_content)
        self.hlayout_process = QtWidgets.QHBoxLayout()
        self.hlayout_process.setObjectName("hlayout_process")
        self.btn_process = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_process.sizePolicy().hasHeightForWidth())
        self.btn_process.setSizePolicy(sizePolicy)
        self.btn_process.setBaseSize(QtCore.QSize(0, 0))
        self.btn_process.setObjectName("btn_process")
        self.hlayout_process.addWidget(self.btn_process)
        self.verticalLayout.addLayout(self.hlayout_process)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_back.setText(_translate("MainWindow", "Back"))
        self.lbl_instructions.setText(_translate("MainWindow", "Select a data file to process: "))
        self.btn_process.setText(_translate("MainWindow", "Process"))

