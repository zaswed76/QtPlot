
from PyQt5 import QtCore


class Action(QtCore.QObject):
    def __init__(self, app, *args):
        super().__init__()
        self.app = app
        self.args = args


    def __call__(self):
        self.run()

    def run(self):
        raise Exception("override the method run")