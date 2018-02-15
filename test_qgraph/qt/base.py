
import sys
from PyQt5 import QtWidgets

class QtGraph(QtWidgets.QFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.plot_creator = PlotCreator()






class PlotCreator():
    def __init__(self):
        pass

    def update_plot(self):
        pass
        """
        получить данные контроллеров
        получить имя метода загрузки данных из базы
        получить имя метода рисования графика
        получить данные
        вызвать метод рисоания  графиков
        """
        control = self.get_control()
        query_method = self.query_method(control)
        plot_method = self.plot_method(control)
        data = self.get_data(query_method)
        self.create_plot(data, plot_method)


    def get_control(self):
        return

    def query_method(self, control):
        return

    def plot_method(self, control):
        return

    def get_data(self, query_method):
        return

    def create_plot(self, data, plot_method):
        pass