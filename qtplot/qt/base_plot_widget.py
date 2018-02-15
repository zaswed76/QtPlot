#! usr/bin/env/ python3

"""

окно которое содержит контроллы и окно рисования графиков
"""



import sys
from PyQt5 import QtWidgets
from PyQt5 import QtCore


from qtplot.qt import canvas
from qtplot.qt import plt_creator


class Controllers():
    def __init__(self):
        pass

class BasePlotWidget(QtWidgets.QFrame):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.box = QtWidgets.QHBoxLayout(self)
        self.btn = QtWidgets.QPushButton("update")
        self.btn.clicked.connect(self.update_plot)
        self.box.addWidget(self.btn)
        self.canvas = canvas.Canvas()
        self.plt_creator = plt_creator.PlotCreator(self.canvas)
        self.box.addWidget(self.canvas)

    def update_plot(self):
        self.plt_creator.update_plot()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # app.setStyleSheet(open('./etc/{0}.qss'.format('style'), "r").read())
    main = BasePlotWidget()
    main.show()
    sys.exit(app.exec_())