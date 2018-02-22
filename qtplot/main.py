#! usr/bin/env/ python3


"""

запуск приложения
"""

import os
import sys
from PyQt5 import QtWidgets, QtCore
from qtplot import resources

ROOT = os.path.join(os.path.dirname(__file__))

CSS_DIR = os.path.join(ROOT, "css")



from qtplot.qt import (mainwidget, message_handler, canvas, base_plot_widget, plt_creator, control, plot_widget_actions)

QtCore.qInstallMessageHandler(message_handler.qt_message_handler)

def main():
    app = QtWidgets.QApplication(sys.argv)
    css_path = os.path.join(CSS_DIR, "main.css")
    app.setStyleSheet(open(css_path, "r").read())
    main_window = mainwidget.MainWidget()

    main_window.show()

    canv = canvas.Canvas()
    plt_fabric = plt_creator.PlotCreator()
    plot_controllers = control.Controllers(plot_widget_actions)
    plot_widget = base_plot_widget.BasePlotWidget(canv,
                                                  plt_fabric,
                                                  controller=plot_controllers,)
    plot_widget.init_tool()
    main_window.add_window(plot_widget)


    sys.exit(app.exec_())


if __name__ == '__main__':
    main()