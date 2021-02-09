"""
main.py -- Launching point for automated distribution package (FBS).
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
# The automated distribution package, Fman Build System (FBS), requires the
# project repository contain a file named "main.py" to launch the application.
# See https://build-system.fman.io


import sys
from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5.QtGui import QImage
from windows import StartWindow


class AppContext(ApplicationContext):
    def __init__(self, *args, **kwargs):
        super(AppContext, self).__init__(*args, **kwargs)

        # define the stylesheet used to customize the appearance of almost all frontend components
        # StyleSheet Examples: https://doc.qt.io/qt-5/stylesheet-examples.html
        style = '''
        /* ---------- SET OVERALL BACKGROUND THEME ---------- */
        QMainWindow {
            background-color: white;
        }
        /* ---------- SET TEXT STYLES FOR MOST WIDGETS ---------- */
        QLabel {
            font-size: 13px;
            font: "Arial";
        }
        QPushButton {
            font-size: 13px;
            font: "Arial";
        }
        QPushButton {
            border: 1px solid #8f8f91;
            border-radius: 3px;
            background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                              stop: 0 #f6f7fa, stop: 1 #dadbde);
            min-width: 110px;
            min-height: 38px;
        }
        QPushButton:pressed {
            background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                              stop: 0 #dadbde, stop: 1 #f6f7fa);
        }
        /* ---------- SET TOOLTIP FONT ---------- */
        QToolTip { 
            font-size: 13px;
            font: "Arial";
            padding: 4px;
        }
        /* ---------- SET "APPLY" and "REFRESH" BUTTONS ---------- */
        #btn_apply_changes {
            border: 1px solid darkblue;
            border-radius: 5px;
            background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                              stop: 0 #e3e6fa, stop: 1 #c3c7db);
            min-width: 110px;
            min-height: 38px;
        }
        #btn_apply_changes:pressed {
            background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                              stop: 0 #c3c7db, stop: 1 #e3e6fa);
        }
        #btn_refresh_plot {
            border: 1px solid darkblue;
            border-radius: 5px;
            background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                              stop: 0 #e3e6fa, stop: 1 #c3c7db);
            min-width: 110px;
            min-height: 38px;
        }
        #btn_refresh_plot:pressed {
            background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                              stop: 0 #c3c7db, stop: 1 #e3e6fa);
        }
        /* ---------- SET "PLAY" BUTTON TO GREEN ---------- */
        #btn_play {
            border: 1px solid #8f8f91;
            border-radius: 3px;
            background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                              stop: 0 #e3fae5, stop: 1 #c3dbc6);
            min-width: 110px;
            min-height: 38px;
        }
        #btn_play:pressed {
            background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                              stop: 0 #c3dbc6, stop: 1 #e3fae5);
        }
        /* ---------- SET "PAUSE" BUTTON TO RED ---------- */
        #btn_pause {
            border: 1px solid #8f8f91;
            border-radius: 3px;
            background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                              stop: 0 #fae3e3, stop: 1 #dbc3c3);
            min-width: 110px;
            min-height: 38px;
        }
        #btn_pause:pressed {
            background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                              stop: 0 #dbc3c3, stop: 1 #fae3e3);
        }
        /* ---------- SET STYLE FOR SCROLL BARS ---------- */
        QScrollBar:vertical {              
            border: 1px solid #999999;
            background:white;
            width: 7px;
            margin: 0px 0px 0px 0px;
        }
        QScrollBar::handle:vertical {
            background: #6a6a6e;
            min-height: 0px;
            border-radius: 3px;
        }
        QScrollBar::add-line:vertical {
            background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
            stop: 0 rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130),  stop:1 rgb(32, 47, 130));
            height: 0px;
            subcontrol-position: bottom;
            subcontrol-origin: margin;
        }
        QScrollBar::sub-line:vertical {
            background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
            stop: 0  rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130),  stop:1 rgb(32, 47, 130));
            height: 0 px;
            subcontrol-position: top;
            subcontrol-origin: margin;
        }
        /* ---------- (LEVEL 4) STYLE THE TAB WIDGET THAT CONTAINS SCROLLABLE AREAS ---------- */
        QTabWidget::pane {
          border: 1px solid darkgray; 
          border-radius: 3px;
          top:-1px; 
          background: rgb(230, 230, 230);
        } 
        QTabBar::tab {
          background: rgb(200, 200, 200); 
          border-radius: 3px;
          border: 1px solid darkgray; 
          padding: 15px;
        } 
        QTabBar::tab:selected { 
          background: rgb(230, 230, 230); 
          margin-bottom: -3px; 
        }
        /* make non-selected tabs look smaller */
        QTabBar::tab:!selected {
            margin-top: 8px;
            margin-bottom: -3px; 
        }
        /* ---------- (LEVEL 3) STYLE THE SCROLLABLE AREAS THAT CONTAIN GROUPBOXES ---------- */
        QScrollArea#scrollArea {
            border: 1px solid darkgray; 
        }       
        QScrollArea#scrollArea_2 {
            border: 1px solid darkgray; 
        }      
        #scrollAreaWidgetContents {
            background-color: rgb(230, 230, 230);
        }
        #scrollAreaWidgetContents_2 {
            background-color: rgb(230, 230, 230);
        }
        /* ---------- (LEVEL 2) STYLE GROUPBOXES THAT CONTAIN SMALLER INPUT WIDGETS ---------- */
        QGroupBox {
            border: 1.5px solid gray;
            border-radius: 3px;
            margin-top: 3ex;
            font: "Arial";
            font-size: 15px;
        }  
        QGroupBox:title {
            subcontrol-origin: margin;
            subcontrol-position: top center;
            font-weight: bold;
        }
        /* ---------- (LEVEL 1) STYLE SMALLER INPUT WIDGETS---------- */
        QLineEdit {
            background: white;
        }  
        QSpinBox {
            background: white;
        }       
        QDoubleSpinBox {
            background: white;
        }       
        QDateTimeEdit {
            background: white;
        }       
        QTimeEdit {
            background: white;
        }       
        '''
        # set the stylesheet
        self.app.setStyleSheet(style)

        # instantiate the initial window to be displayed when opening the application
        self.start_window = StartWindow(self)

    def run(self):
        # show the initial window
        self.start_window.show()
        return self.app.exec_()

    def img_parse_logo(self):
        # load the large PARSE graphic to be shown on the start window
        return QImage(self.get_resource('PARSE_logo.png'))

    def img_usc_logo(self):
        # load the small USC logo to be shown on the start window
        return QImage(self.get_resource('usc_logo_2.png'))

    def img_custom_logo(self):
        # load the custom PARSE icon graphic, unused at present (02.2021)
        return QImage(self.get_resource('custom_logo_256.png'))

    # todo: cached?
    def img_info_icon(self):
        # load the info icon graphic, used for tooltips
        return QImage(self.get_resource('info_icon.png'))


if __name__ == '__main__':
    appctxt = AppContext()
    exit_code = appctxt.run()
    sys.exit(exit_code)
