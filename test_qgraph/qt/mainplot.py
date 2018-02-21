


import sys
from PyQt5 import QtWidgets, QtCore

class Btn(QtWidgets.QPushButton):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.setObjectName(self.text())
        self.setCheckable(True)

    def __repr__(self):
        return "{}- {}".format(self.__class__.__name__, self.objectName())




class PlotWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self._controllers =  None
        self.resize(500, 500)
        self.box = QtWidgets.QHBoxLayout(self)


    @property
    def controllers(self):
        return self._controllers

    @controllers.setter
    def controllers(self, control_m):
        self._controllers = control_m
        # self._controllers.set_app(self)

    def init_tools(self):
        group_btn = QtWidgets.QButtonGroup()
        group_btn.setObjectName("btn_group")
        group_btn.setExclusive(False)
        for n in range(4):
            l = str(n)
            btn = Btn(l)
            group_btn.addButton(btn)
            self.box.addWidget(btn)
        self.controllers.register_group(group_btn, "clicked", "Update", 5, 7)







if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # app.setStyleSheet(open('./etc/{0}.qss'.format('style'), "r").read())
    main = PlotWidget()
    main.show()
    sys.exit(app.exec_())