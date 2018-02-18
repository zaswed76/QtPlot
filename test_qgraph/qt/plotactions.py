

from PyQt5.QtCore import pyqtSlot
import sys
from PyQt5 import QtWidgets, QtCore


class Action(QtCore.QObject):
    def __init__(self, app, *args):
        super().__init__()
        self.app = app
        self.args = args


    def __call__(self):
        self.run()

    def run(self):
        raise Exception("override the method run")




@pyqtSlot()
class Update(Action):
    def __init__(self, app, *args):
        super().__init__(app)
        self.app = app
        self.args = args

    def run(self):
        group = self.app.controllers.group["btn_group"]
        res = []
        for c in group.buttons():
            if c.isChecked():
                res.append(c)
        print(res)




if __name__ == '__main__':
    up = Update()
    up()