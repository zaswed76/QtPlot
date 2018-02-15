

import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import pyqtSignal, QObject
from test_qgraph.graph import axes

def qt_message_handler(mode, context, message):
    if mode == QtCore.QtInfoMsg:
        mode = 'INFO'
    elif mode == QtCore.QtWarningMsg:
        mode = 'WARNING'
    elif mode == QtCore.QtCriticalMsg:
        mode = 'CRITICAL'
    elif mode == QtCore.QtFatalMsg:
        mode = 'FATAL'
    else:
        mode = 'DEBUG'
    print('qt_message_handler: line: %d, func: %s(), file: %s' % (
        context.line, context.function, context.file))
    print('  %s: %s\n' % (mode, message))


QtCore.qInstallMessageHandler(qt_message_handler)





class Scene(QtWidgets.QGraphicsScene):
    def __init__(self, size):
        super().__init__()

        self.setSceneRect(0, 0, *size)
        self.setBackgroundBrush(QtGui.QColor("#FFFFFF"))


    def on_changed_value(self, v):
        print(v)

class Graph(QtWidgets.QGraphicsView):
    def __init__(self, size):
        super().__init__()
        # self.setFl
        self.scale(1, -1)
        self.setFrameStyle(QtWidgets.QFrame.NoFrame | QtWidgets.QFrame.NoFrame)
        self.setFixedSize(size[0]+2, size[1]+2)
        self.scene = Scene(size)
        self.setScene(self.scene)
        self.setStyleSheet("background-color: green")

    def set_axes(self, ax_cfg=None):
        if ax_cfg is None: ax_cfg = {}
        ax = axes.Axes(self,  cfg=ax_cfg)
        self.scene.addItem(ax)









if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # app.setStyleSheet(open('./etc/{0}.qss'.format('style'), "r").read())
    graph = Graph((600, 500))
    ax_cfg = {"color": "darkcyan", "margin": {"left": 50, "bottom": 50}, "width_line": 0.7}
    graph.set_axes()

    graph.show()
    sys.exit(app.exec_())

