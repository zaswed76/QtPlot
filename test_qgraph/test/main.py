import sys
from PyQt5 import QtWidgets, QtCore
import random
from test_qgraph.test import plot_widget
from test_qgraph.plot import axis
from test_qgraph import message_handler
QtCore.qInstallMessageHandler(message_handler.qt_message_handler)

class Tool(QtWidgets.QFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.box = QtWidgets.QVBoxLayout(self)
        self.update_btn = QtWidgets.QPushButton("1")
        self.update_btn.setStyleSheet("background-color: white")
        self.box.addWidget((self.update_btn))

        self.creat_btn = QtWidgets.QPushButton("2")
        self.creat_btn.setStyleSheet("background-color: white")
        self.box.addWidget((self.creat_btn))

        self.creat_btn2 = QtWidgets.QPushButton("3")
        self.creat_btn2.setStyleSheet("background-color: white")
        self.box.addWidget((self.creat_btn2))

class Widget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.box = QtWidgets.QHBoxLayout(self)
        self.tool = Tool()
        self.tool.setFixedWidth(70)
        self.tool.setStyleSheet("background-color: grey")
        self.box.addWidget(self.tool)
        self.graph_widget = plot_widget.MatplotlibWidget()
        self.graph_widget.setStyleSheet("background-color: green")
        self.box.addWidget(self.graph_widget)

        self.canvas = self.graph_widget.canvas
        self.resize(1200, 700)



        self.canvas.mpl_connect('pick_event', self.on_pick)
        self.tool.update_btn.clicked.connect(self.create_subplot)
        self.tool.creat_btn.clicked.connect(self.create_subplot2)
        self.tool.creat_btn2.clicked.connect(self.create_subplot3)

    def create_plot(self):
        pass

    def create_subplot(self):
        self.graph_widget.clear()
        a = self.graph_widget.set_axis(axis.Axis.OneAxis)
        self.canvas.draw()

    def create_subplot2(self):
        self.graph_widget.clear()
        a, b = self.graph_widget.set_axis(axis.Axis.Two_axis)
        self.canvas.draw()

    def create_subplot3(self):
        self.graph_widget.clear()
        a, b, s = self.graph_widget.set_axis(axis.Axis.Three_axis)
        self.canvas.draw()

    def update_plot(self):
        self.graph_widget.axis.clear()
        x = list(range(1, 23))
        y = [1,1, 3,4,7,8,4,9,11,13,12,14,12,7,8,5,9,9,9,5,4,3]
        #
        # self.ax.bar(x, y, width=0.9, color="green", label="vis", picker=5)
        # random.shuffle(y)
        # print(len(x))
        # print(len(y))
        self.ax.set_ylim(0, 50)
        self.ax.plot(x, y, color="cyan", label="Les")
        # random.shuffle(y)
        # self.ax.plot(x, y, color="green", label="troya")
        #
        # random.shuffle(y)
        # self.ax.plot(x, y, color="#D89004", label="aka")
        # self.ax.legend()
        # random.shuffle(y)
        # self.ax.bar(x, y, width=0.6, color="red", label="pro")
        # random.shuffle(y)
        # self.ax.bar(x, y, width=0.3, color="y", label="sch")

        self.canvas.draw()



    def on_pick(self, e):
        a = e.artist
        print(a.get_x() + a.get_width()/2)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # app.setStyleSheet(open('./etc/{0}.qss'.format('style'), "r").read())
    main = Widget()
    main.show()
    sys.exit(app.exec_())