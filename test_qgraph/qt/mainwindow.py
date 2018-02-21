

import sys
from PyQt5 import QtWidgets

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.central_widget = QtWidgets.QFrame()
        self.setCentralWidget(self.central_widget)
        self.stack = QtWidgets.QStackedLayout(self.central_widget)


    @property
    def controllers(self):
        return self._controllers

    @controllers.setter
    def controllers(self, control_m):
        self._controllers = control_m
        # self._controllers.set_app(self)

    def add_widget(self, widget):
        self.stack.addWidget(widget)

    def init_menu(self):
        action = QtWidgets.QAction("update", self)
        self.controllers.register(action, "triggered", "Update", 5, 7)
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(action)





if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # app.setStyleSheet(open('./etc/{0}.qss'.format('style'), "r").read())
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())