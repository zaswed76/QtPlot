


class PlotCreator():
    def __init__(self, canvas):
        self.canvas = canvas

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
        return "plot_one_axis"

    def get_data(self, query_method):
        return

    def create_plot(self, data, plot_method):
        getattr(self, plot_method)(data)

    def plot_one_axis(self, data):
        canvas = self.canvas
        canvas.plot(data)