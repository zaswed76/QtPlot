
from PyQt5 import QtCore


class Controllers(QtCore.QObject):
    def __init__(self, app, actions_module):
        super().__init__()
        self.app = app
        self.actions_module = actions_module
        self._controls = {}
        self._groups = {}

    def set_app(self, app):
        self.app = app

    def register(self, control, signal, action, *args):
        self._controls[control.objectName()] = control
        getattr(control, signal).connect(getattr(self.actions_module, action)(self.app, *args))


    def register_group(self, group, signal, action, *args):
        self._groups[group.objectName()] = group
        for control in group.buttons():
            self.register(control, signal, action, *args)

    @property
    def groups(self):
        return self._groups

    @property
    def controls(self):
        return self._controls