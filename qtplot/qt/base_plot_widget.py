#! usr/bin/env/ python3

"""

окно которое содержит контроллы и окно рисования графиков
"""


import sys
from PyQt5 import QtWidgets, QtCore



class Controllers():
    def __init__(self):
        pass

class BasePlotWidget(QtWidgets.QFrame):
    def __init__(self, canvas, plt_creator, controller=None):
        super().__init__()
        self._controller = controller
        if self._controller is not None:
            self._controller.set_app(self)
        self.box = QtWidgets.QHBoxLayout(self)



        self.plt_creator = plt_creator
        self.plt_creator.canvas = canvas
        self.box.addWidget(canvas)

    def init_tool(self):

        self.btn = QtWidgets.QPushButton()
        self.btn.setIconSize(QtCore.QSize(32, 32))
        self.btn.setFixedSize(32, 32)
        self.btn.setObjectName("update_btn")
        self.box.insertWidget(0, self.btn)
        self.controller.register(self.btn, "clicked", "Update")

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller
        self._controller.set_app(self)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # app.setStyleSheet(open('./etc/{0}.qss'.format('style'), "r").read())
    main = BasePlotWidget()
    main.show()
    sys.exit(app.exec_())