#! usr/bin/env/ python3


"""

запуск приложения
"""

import sys
from PyQt5 import QtWidgets, QtCore

from qtplot.qt import base_plot_widget, message_handler

QtCore.qInstallMessageHandler(message_handler.qt_message_handler)

def main():
    app = QtWidgets.QApplication(sys.argv)
    # app.setStyleSheet(open('./etc/{0}.qss'.format('style'), "r").read())
    main = base_plot_widget.BasePlotWidget()
    main.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()