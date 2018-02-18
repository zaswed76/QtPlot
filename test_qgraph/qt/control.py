import sys
from PyQt5 import QtWidgets, QtCore

class Controllers(QtCore.QObject):
    def __init__(self, actions_module):
        super().__init__()
        self.actions_module = actions_module
        self._controls = {}
        self._group = {}

    def set_app(self, app):
        self.app = app

    def register(self, control, signal, action, *args):
        self._controls[control.objectName()] = control
        getattr(control, signal).connect(getattr(self.actions_module, action)(self.app, *args))


    def register_group(self, group, signal, action, *args):
        self._group[group.objectName()] = group
        for control in group.buttons():
            self.register(control, signal, action, *args)

    @property
    def group(self):
        return self._group

    @property
    def controls(self):
        return self._controls