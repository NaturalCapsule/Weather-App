from display_weather_info import Ui_MainWindow
from PyQt6 import QtWidgets
import sys


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow(MainWindow)
    ui.setupUi()
    MainWindow.show()
    sys.exit(app.exec())