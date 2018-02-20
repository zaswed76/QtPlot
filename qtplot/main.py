#! usr/bin/env/ python3


"""

запуск приложения
"""

import os

ROOT = os.path.join(os.path.dirname(__file__))

CSS_DIR = os.path.join(ROOT, "css")

import sys
from PyQt5 import QtWidgets, QtCore

from qtplot.qt import mainwidget, message_handler


QtCore.qInstallMessageHandler(message_handler.qt_message_handler)

def main():

    app = QtWidgets.QApplication(sys.argv)
    css_path = os.path.join(CSS_DIR, "main.css")
    app.setStyleSheet(open(css_path, "r").read())
    main = mainwidget.MainWidget()
    main.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()