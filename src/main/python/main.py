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
        /* ---------- (LEVEL 4) STYLE THE TAB WIDGET THAT CONTAINS SCROLLABLE AREAS ---------- */
        QTabWidget::pane {
          border: 1px solid darkgray; 
          top:-1px; 
          background: rgb(230, 230, 230);
        } 
        QTabBar::tab {
          background: rgb(200, 200, 200); 
          border: 1px solid darkgray; 
          padding: 15px;
        } 
        QTabBar::tab:selected { 
          background: rgb(230, 230, 230); 
          margin-bottom: -1px; 
        }
        /* make non-selected tabs look smaller */
        QTabBar::tab:!selected {
            margin-top: 8px;
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


if __name__ == '__main__':
    appctxt = AppContext()
    exit_code = appctxt.run()
    sys.exit(exit_code)
