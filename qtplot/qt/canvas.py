import random

import sys
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
import matplotlib as mpl
from PyQt5 import QtGui, QtCore, QtWidgets

from test_qgraph.plot import axis
from test_qgraph import message_handler


class Canvas(QtWidgets.QFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.figure = Figure()
        self.canvas = FigureCanvasQTAgg(self.figure)
        self.layoutVertical = QtWidgets.QVBoxLayout(self)
        self.layoutVertical.setSpacing(0)
        self.layoutVertical.setContentsMargins(0, 0, 0, 0)
        self.layoutVertical.addWidget(self.canvas)


    def set_axis(self, name):
        ax = axis.Axis(self.figure)
        return ax(name)

    def clear(self):
        self.figure.clear()

    def plot(self, data):
        print("plot", data)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # app.setStyleSheet(open('./etc/{0}.qss'.format('style'), "r").read())
    main = Canvas()
    main.show()
    ax = main.set_axis(axis.Axis.OneAxis)

    sys.exit(app.exec_())