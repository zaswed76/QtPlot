

#!/usr/bin/env python3

import sys
from PyQt5 import QtWidgets, QtCore



class Widget(QtWidgets.QFrame):
    def __init__(self):
        super().__init__()
        self.resize(1200, 800)
        self.box = QtWidgets.QHBoxLayout(self)
        self.setStyleSheet("background-color: #E3E3E3")
        # self.showFullScreen()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # app.setStyleSheet(open('./etc/{0}.qss'.format('style'), "r").read())
    main = Widget()
    main.show()
    sys.exit(app.exec_())