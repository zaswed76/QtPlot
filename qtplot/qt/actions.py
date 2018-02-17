

class UpdateControls():
    def __init__(self, app, *args):
        self.app = app
        self.run(*args)

    def run(self, control):
        self.app.base_method(control.text())
