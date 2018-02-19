from PyQt5.QtCore import pyqtSlot
from test_qgraph.qt import action


@pyqtSlot()
class Update(action.Action):
    def __init__(self, app, *args):
        super().__init__(app)
        self.app = app
        self.args = args

    def run(self):
        print(self.app, self.args)
