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
        style = ''' 
        QMainWindow {
                    background-color: white;
        }
        QGroupBox {
            border: 1.5px solid gray;
            border-radius: 3px;
            margin-top: 4ex;
            font: 11pt "Arial";
        }  
        QGroupBox:title {
            subcontrol-origin: margin;
            padding: 5 0px;
            font: 11pt "Arial";
        }
        '''
        self.app.setStyleSheet(style)

        self.start_window = StartWindow(self)

    def run(self):
        self.start_window.show()
        return self.app.exec_()

    def img_parse_logo(self):
        return QImage(self.get_resource('PARSE_logo.png'))

    def img_usc_logo(self):
        return QImage(self.get_resource('usc_logo_2.png'))

    def img_custom_logo(self):
        return QImage(self.get_resource('custom_logo_256.png'))


if __name__ == '__main__':
    appctxt = AppContext()
    exit_code = appctxt.run()
    sys.exit(exit_code)
