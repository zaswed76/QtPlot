
from functools import partial
from PyQt5.QtCore import QObject



class ControlManager(QObject):
    def __init__(self, app, actions_mod):
        super().__init__()
        self.actions_mod = actions_mod
        self.app = app
        self._controls = {}

    def register(self, btn, signal, method):
        self._controls[btn.objectName()] = btn
        getattr(btn, signal).connect(partial(self.run_action, method, btn))


    def run_action(self, action, btn):
        getattr(self.actions_mod, action)(self.app, btn)


    @property
    def controls(self):
        return self._controls.values()