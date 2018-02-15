#! usr/bin/env/ python3

"""

модуль предоставляет класс который выводит графики
"""
from PyQt5 import QtWidgets, QtCore

class Canvas(QtWidgets.QLabel):
    def __init__(self):
        super().__init__()
        self.setFixedSize(400, 400)
        self.setAlignment(QtCore.Qt.AlignCenter)

    def plot(self, data):
        self.clear()
        self.setText("нарисовали график")