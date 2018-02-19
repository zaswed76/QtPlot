from PyQt5.QtCore import pyqtSlot
from test_qgraph.qt import action


@pyqtSlot()
class Update(action.Action):
    def __init__(self, app, *args):
        super().__init__(app)
        self.app = app
        self.args = args

    def run(self):
        group = self.app.controllers.groups["btn_group"]
        res = []
        for c in group.buttons():
            if c.isChecked():
                res.append(c)
        print(res)


if __name__ == '__main__':
    up = Update()
    up()
