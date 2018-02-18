import sys
from PyQt5 import QtWidgets, QtCore

from test_qgraph.qt import (mainplot, control, plotactions,
                            mainwindow, mainactions)

def qt_message_handler(mode, context, message):
    if mode == QtCore.QtInfoMsg:
        mode = 'INFO'
    elif mode == QtCore.QtWarningMsg:
        mode = 'WARNING'
    elif mode == QtCore.QtCriticalMsg:
        mode = 'CRITICAL'
    elif mode == QtCore.QtFatalMsg:
        mode = 'FATAL'
    else:
        mode = 'DEBUG'
    print('qt_message_handler: line: %d, func: %s(), file: %s' % (
        context.line, context.function, context.file))
    print('  %s: %s\n' % (mode, message))


QtCore.qInstallMessageHandler(qt_message_handler)

def main():


    app = QtWidgets.QApplication(sys.argv)

    main_window = mainwindow.MainWindow()
    control_main_manager = control.Controllers(mainactions)
    main_window.control_manager = control_main_manager


    # создаём окно
    plot_widget = mainplot.PlotWidget()
    # создаём объкт контроллера
    # plotactions - ссылка на модуль где определены пользовательские действия
    controllers = control.Controllers(plotactions)
    # передаём контроллер в окно
    plot_widget.controllers = controllers
    # создаём контролы
    plot_widget.init_tools()

    main_window.show()




    sys.exit(app.exec_())

if __name__ == '__main__':
    main()