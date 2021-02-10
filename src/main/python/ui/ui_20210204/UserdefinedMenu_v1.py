# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UserdefinedMenu_v1.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(581, 345)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setContentsMargins(-1, -1, -1, 18)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_back = QtWidgets.QPushButton(self.centralwidget)
        self.btn_back.setObjectName("btn_back")
        self.horizontalLayout.addWidget(self.btn_back)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, 20, -1, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lbl_instructions = QtWidgets.QLabel(self.centralwidget)
        self.lbl_instructions.setObjectName("lbl_instructions")
        self.horizontalLayout_3.addWidget(self.lbl_instructions)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(-1, 20, -1, 20)
        self.gridLayout.setHorizontalSpacing(20)
        self.gridLayout.setVerticalSpacing(12)
        self.gridLayout.setObjectName("gridLayout")
        self.lbl_lcp = QtWidgets.QLabel(self.centralwidget)
        self.lbl_lcp.setObjectName("lbl_lcp")
        self.gridLayout.addWidget(self.lbl_lcp, 1, 0, 1, 1)
        self.lbl_rcp = QtWidgets.QLabel(self.centralwidget)
        self.lbl_rcp.setObjectName("lbl_rcp")
        self.gridLayout.addWidget(self.lbl_rcp, 0, 0, 1, 1)
        self.lbl_bandfreq = QtWidgets.QLabel(self.centralwidget)
        self.lbl_bandfreq.setObjectName("lbl_bandfreq")
        self.gridLayout.addWidget(self.lbl_bandfreq, 2, 0, 1, 1)
        self.spin_bandfreq = QtWidgets.QSpinBox(self.centralwidget)
        self.spin_bandfreq.setMaximum(30000)
        self.spin_bandfreq.setProperty("value", 2300)
        self.spin_bandfreq.setObjectName("spin_bandfreq")
        self.gridLayout.addWidget(self.spin_bandfreq, 2, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        spacerItem1 = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.btn_continue = QtWidgets.QPushButton(self.centralwidget)
        self.btn_continue.setMinimumSize(QtCore.QSize(120, 0))
        self.btn_continue.setObjectName("btn_continue")
        self.horizontalLayout_2.addWidget(self.btn_continue)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.setStretch(4, 10)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_back.setText(_translate("MainWindow", "Back"))
        self.lbl_instructions.setText(_translate("MainWindow", "For instructions on how to format User-Defined data files\n"
"please see the User\'s Guide."))
        self.lbl_lcp.setText(_translate("MainWindow", "Select the LCP data file:"))
        self.lbl_rcp.setText(_translate("MainWindow", "Select the RCP data file:"))
        self.lbl_bandfreq.setText(_translate("MainWindow", "Enter the band (antenna) frequency:"))
        self.spin_bandfreq.setSuffix(_translate("MainWindow", " MHz"))
        self.btn_continue.setText(_translate("MainWindow", "Continue"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

