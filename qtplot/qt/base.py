

import sys
from PyQt5 import QtWidgets, QtCore

from qt import message_handler, control_manager, actions

message_handler.main()

class Btn(QtWidgets.QPushButton):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.setCheckable(True)

class Widget(QtWidgets.QFrame):
    def __init__(self):
        super().__init__()
        self.act = control_manager.ControlManager(self, actions)
        self.resize(500, 500)
        self.box = QtWidgets.QHBoxLayout(self)

        self.up_btn = Btn("update1", self)
        self.act.register(self.up_btn, "clicked", "UpdateControls")

        self.up_btn2 =Btn("update2", self)
        self.up_btn2.move(100, 0)
        self.act.register(self.up_btn2, "clicked", "UpdateControls")

        self.up_btn3 =QtWidgets.QPushButton("3", self)
        self.up_btn3.move(400, 0)
        self.act.register(self.up_btn3, "clicked", "UpdateControls")

    def base_method(self, *args):
        print(args[0])


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # app.setStyleSheet(open('./etc/{0}.qss'.format('style'), "r").read())
    main = Widget()
    main.show()
    sys.exit(app.exec_())