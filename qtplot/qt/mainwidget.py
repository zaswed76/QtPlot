#!/usr/bin/env python3

"""

class MainWidget главное окно организовнанное с помощью QStackedLayout
"""
import sys
from PyQt5 import QtWidgets, QtCore


class MainWidget(QtWidgets.QMainWindow):
    def __init__(self, cfg=None):
        super().__init__()
        self.cfg = cfg
        self.central_widget = QtWidgets.QFrame()
        self.setCentralWidget(self.central_widget)
        self.stack = QtWidgets.QStackedLayout(self.central_widget)

    def add_window(self, window):
        self.stack.addWidget(window)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # app.setStyleSheet(open('./etc/{0}.qss'.format('style'), "r").read())
    main = MainWidget()
    main.show()
    sys.exit(app.exec_())