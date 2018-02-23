from qtplot.plot import axis


class Plotter:
    def __init__(self):
        pass

    @staticmethod
    def bar(ax, data1, data2, **kwargs):
        plot = ax.bar(data1, data2, **kwargs)




class PlotCreator():
    def __init__(self, canvas=None):
        self._canvas = canvas

    def update_canvas(self):
        """
        получить данные контроллеров
        получить имя метода загрузки данных из базы
        получить имя метода рисования графика
        получить данные
        вызвать метод рисоания  графиков
        """

        data_control = self.get_control()
        query_method = self.query_method(data_control)
        plot_method = self.plot_method(data_control)
        data = self.get_data(query_method)

        self.create_plot(data, plot_method)

    @property
    def canvas(self):
        return self._canvas

    @canvas.setter
    def canvas(self, canvas):
        self._canvas = canvas

    def get_control(self):
        return

    def query_method(self, control):
        return

    def plot_method(self, control):
        """

        :param control: cловарь данных контроллеров окна
        :return: имя плоттера
        """
        return "bar"

    def get_data(self, query_method):
        return

    def create_plot(self, data, plot_method):
        getattr(self, plot_method)(data)



    def bar(self, data):
        canvas = self.canvas
        data1 = [3, 5, 8]
        data3 = [2, 4, 7]
        data2 = [1, 2, 3]

        ax = canvas.set_axis(axis.Axis.OneAxis)
        Plotter.bar(ax, data2, data1, picker=True, gid=0)
        Plotter.bar(ax, data2, data3, width=0.5, picker=True, gid=1)
        canvas.resize(700, 500)
