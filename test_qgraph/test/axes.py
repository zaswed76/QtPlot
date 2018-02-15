#! usr/bin/env/ python3

"""

the module provides a class for drawing axes coordinates
>>> import sys
>>> from PyQt5 import QtWidgets, QtCore, QtGui
>>> from test_qgraph.graph import graph
>>> app = QtWidgets.QApplication(sys.argv)
>>> gr = graph.Graph((600, 500))
>>> ax_cfg = {"color": "darkcyan", "margin": {"left": 50, "bottom": 50}, "width_line": 0.7}
>>> gr.set_axes(ax_cfg=ax_cfg)
>>> gr.show()

"""

import copy
from PyQt5 import QtWidgets, QtCore, QtGui

_opt = dict(
    color="darkgrey",
    width_line=1,
    margin={"left": 40, "top": 70, "right": 10, "bottom": 40}

)

def ddd():
    return "test"

class Axes(QtWidgets.QGraphicsItem):
    def __init__(self, scene, **kwargs):
        """
        class drawing axes coordinates
        :param scene: QtWidgets.QGraphicsScene
        :param kwargs:
        cfg = {color:str, width_line:int or float,
               margin: {"left": int, "top": int, "right": int, "bottom": int}}
        """
        super().__init__()
        self.scene = scene
        self.scene_rect = self.scene.sceneRect()
        _cfg = kwargs.get("cfg", dict())
        margin = _opt["margin"]
        margin.update(_cfg.get("margin", {}))
        _cfg.get("margin", {}).update(margin)
        _opt.update(_cfg)
        self.cfg = copy.deepcopy(_opt)
        self.width = self.scene_rect.width()
        self.height = self.scene_rect.height()
        self.setPos(*kwargs.get("pos", (self.cfg["margin"]["left"],
                                        self.cfg["margin"]["bottom"])))
        self.color = self.cfg["color"]
        self.width_line = self.cfg["width_line"]
        self.pen = QtGui.QPen(QtGui.QColor(self.color), self.width_line,
                                  QtCore.Qt.SolidLine)


    def set_pen(self, pen):
        self.pen = pen

    def paint(self, painter, option=None, widget=None):
        self.__draw_rect(painter)



    def boundingRect(self):
        return QtCore.QRectF(0, 0, self.width, self.height)

    def set_y_max(self, max):
        pass

    def __draw_rect(self, p):
        p.setPen(self.pen)
        w = self.width - self.cfg["margin"]["left"] - self.cfg["margin"]["right"]
        h = self.height - self.cfg["margin"]["bottom"] - self.cfg["margin"]["top"]
        rect = QtCore.QRectF(0, 0, w, h)
        p.drawRect(rect)


    def __str__(self):
        return ""


if __name__ == '__main__':
    import doctest
    doctest.testmod()