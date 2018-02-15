

import sys
from PyQt5 import QtWidgets

from test_qgraph.graph import *


# class Widget(QtWidgets.QFrame):
#     def __init__(self):
#         super().__init__()
#         self.resize(1100, 580)
#         self.box = QtWidgets.QHBoxLayout(self)
#         self.tool = QtWidgets.QFrame()
#         self.tool.setStyleSheet("background-color: grey")
#         self.tool.setFixedWidth(170)
#         self.box.addWidget(self.tool)
#         self.graph = graph.Graph((900, 600))
#         self.graph.set_axes()
#         self.box.addWidget(self.graph)
#
# if __name__ == '__main__':
#     app = QtWidgets.QApplication(sys.argv)
#     # app.setStyleSheet(open('./etc/{0}.qss'.format('style'), "r").read())
#     main = Widget()
#     main.show()
#     sys.exit(app.exec_())