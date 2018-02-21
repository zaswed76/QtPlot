#! usr/bin/env/ python3

"""

окно которое содержит контроллы и окно рисования графиков
"""


import sys
from PyQt5 import QtWidgets



class Controllers():
    def __init__(self):
        pass

class BasePlotWidget(QtWidgets.QFrame):
    def __init__(self, controllers, canvas, plt_creator):
        super().__init__()
        self.controller = controllers

        self.box = QtWidgets.QHBoxLayout(self)
        self.btn = QtWidgets.QPushButton("update")
        # self.controller.register(self.btn, "clicked", "Update")

        self.box.addWidget(self.btn)
        self.plt_creator = plt_creator
        self.plt_creator.canvas = canvas
        self.box.addWidget(canvas)

    def update_canvas(self):
        self.plt_creator.update_canvas()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # app.setStyleSheet(open('./etc/{0}.qss'.format('style'), "r").read())
    main = BasePlotWidget()
    main.show()
    sys.exit(app.exec_())