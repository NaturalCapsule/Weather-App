from PyQt6 import QtCore, QtGui, QtWidgets
from qfluentwidgets import FluentWindow, PushButton
import httpx
import os
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtCore import Qt
from io import BytesIO
from get_weather_info import WeatherInfo


class Ui_MainWindow(object):

    def on_pushButton_clicked(self):
        weather_info = WeatherInfo()
        data, icon_url = weather_info.get_json_weather_data()
        # Set weather icon
        if icon_url.startswith("http"):
            image_response = httpx.get(icon_url)
            img_data = BytesIO(image_response.content)
            pixmap = QPixmap()
            pixmap.loadFromData(img_data.read())
            self.label_3.setPixmap(pixmap)
        else:
            print("⚠️ Missing icon URL!")

        # Set weather text
        self.display_condition = str(data['current_condition'][0]['weatherDesc'][0]['value'])
        self.display_temp = str(data['current_condition'][0]['temp_C'])
        self.display_time = str(data['weather'][0]['hourly'][2]['time'])

        if self.display_temp <= "20":
            self.label.setPixmap(QPixmap(u"assets/cold.png"))
        elif self.display_temp > "20" and self.display_temp <= "30":
            self.label.setPixmap(QPixmap(u"assets/warm.png"))
        else:
            self.label.setPixmap(QPixmap(u"assets/hot.png"))

        self.label_1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_1.setText(self.display_temp + "°C")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_4.setText(self.display_condition)
        self.label_2.setText("Forecast Time")
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_6.setText(self.format_weather_times(data)[2])

    def format_weather_times(self, data):
        self.hourly_data = data['weather'][0]['hourly']
        self.times = []

        for self.hour in self.hourly_data:
            self.time_raw = self.hour['time']         # e.g., "600"
            self.time_str = self.time_raw.zfill(4)    # make sure it's 4 digits: "600" → "0600"
            self.formatted = f"{self.time_str[:2]}:{self.time_str[2:]}"  # "0600" → "06:00"
            self.times.append(self.formatted)

        return self.times



    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(650, 461)
        self.icon_path = os.path.abspath("assets/weather-app.ico")
        MainWindow.setWindowIcon(QIcon(self.icon_path))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.frame_3 = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_7.setObjectName("gridLayout_7")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_7.addItem(spacerItem, 1, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_7.addItem(spacerItem1, 0, 3, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(51, 78, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_7.addItem(spacerItem2, 1, 4, 2, 1)
        self.label_2 = QtWidgets.QLabel(parent=self.frame_3)
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_2.setStyleSheet("""
    QLabel {
        color: black;
        background-color: white;
        border-radius: 10px;
        padding: 10px;
        font-size: 18px;
        font-weight: bold;
        font-family: Arial;
    }
""")
        self.gridLayout_7.addWidget(self.label_2, 1, 3, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(51, 78, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_7.addItem(spacerItem3, 1, 2, 2, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_7.addItem(spacerItem4, 1, 5, 1, 1)
        self.label_6 = QtWidgets.QLabel(parent=self.frame_3)
        self.label_6.setText("")
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.label_6.setStyleSheet("""
    QLabel {
        color: black;
        background-color: white;
        border-radius: 10px;
        padding: 10px;
        font-size: 18px;
        font-weight: bold;
        font-family: Arial;
    }
""")
        self.gridLayout_7.addWidget(self.label_6, 2, 3, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_7.addItem(spacerItem5, 3, 3, 1, 1)
        self.gridLayout_6.addWidget(self.frame_3, 0, 3, 1, 1)
        self.frame_4 = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_8.setObjectName("gridLayout_8")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_8.addItem(spacerItem6, 2, 5, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_8.addItem(spacerItem7, 0, 2, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_8.addItem(spacerItem8, 2, 1, 2, 1)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_8.addItem(spacerItem9, 2, 4, 2, 1)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_8.addItem(spacerItem10, 4, 2, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_8.addItem(spacerItem11, 2, 0, 1, 1)
        self.label_1 = QtWidgets.QLabel(parent=self.frame_4)
        self.label_1.setStyleSheet("""
    QLabel {
        color: black;
        background-color: white;
        border-radius: 10px;
        padding: 10px;
        font-size: 18px;
        font-weight: bold;
        font-family: Arial;
    }
""")
        self.gridLayout_8.addWidget(self.label_1, 3, 2, 1, 1)
        self.label = QtWidgets.QLabel(parent=self.frame_4)
        self.label.setEnabled(True)
        self.label.setMouseTracking(False)
        self.label.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label.setText("")
        self.label.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.gridLayout_8.addWidget(self.label, 2, 2, 1, 1)
        self.gridLayout_6.addWidget(self.frame_4, 0, 1, 1, 1)
        self.frame_2 = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_5.setObjectName("gridLayout_5")
        spacerItem12 = QtWidgets.QSpacerItem(51, 88, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_5.addItem(spacerItem12, 1, 1, 2, 1)
        spacerItem13 = QtWidgets.QSpacerItem(51, 88, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_5.addItem(spacerItem13, 1, 3, 2, 1)
        spacerItem14 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_5.addItem(spacerItem14, 0, 2, 1, 1)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_5.addItem(spacerItem15, 1, 4, 1, 1)
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_5.addItem(spacerItem16, 1, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(parent=self.frame_2)
        self.label_4.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label_4.setText("")
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_4.setStyleSheet("""
    QLabel {
        color: black;
        background-color: white;
        border-radius: 10px;
        padding: 10px;
        font-size: 18px;
        font-weight: bold;
        font-family: Arial;
    }
""")

        self.gridLayout_5.addWidget(self.label_4, 2, 2, 1, 1)
        spacerItem17 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_5.addItem(spacerItem17, 3, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(parent=self.frame_2)
        self.label_3.setText("")
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.gridLayout_5.addWidget(self.label_3, 1, 2, 1, 1)
        self.gridLayout_6.addWidget(self.frame_2, 0, 0, 1, 1)
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.pushButton = PushButton(parent=self.frame)
        self.pushButton.setStyleSheet("QPushButton {\n"
"    color: white;\n"
"    font-weight: bold;\n"
"    border: none;\n"
"    border-radius: 12px;\n"
"    padding: 10px;\n"
"    background: qlineargradient(\n"
"        x1:0, y1:0, x2:1, y2:0,\n"
"        stop:0 #00C853, stop:1 #2196F3\n"
"    );\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(\n"
"        x1:0, y1:0, x2:1, y2:0,\n"
"        stop:0 #00E676, stop:1 #64B5F6\n"
"    );\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background: qlineargradient(\n"
"        x1:0, y1:0, x2:1, y2:0,\n"
"        stop:0 #00A844, stop:1 #1976D2\n"
"    );\n"
"}\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.on_pushButton_clicked)
        self.gridLayout_3.addWidget(self.pushButton, 1, 2, 1, 1)
        spacerItem18 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_3.addItem(spacerItem18, 1, 4, 1, 1)
        spacerItem19 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_3.addItem(spacerItem19, 0, 2, 1, 1)
        spacerItem20 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_3.addItem(spacerItem20, 1, 0, 1, 1)
        spacerItem21 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_3.addItem(spacerItem21, 1, 3, 1, 1)
        spacerItem22 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_3.addItem(spacerItem22, 1, 1, 1, 1)
        spacerItem23 = QtWidgets.QSpacerItem(145, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_3.addItem(spacerItem23, 2, 2, 1, 1)
        self.gridLayout_6.addWidget(self.frame, 1, 0, 1, 4)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Weather App"))
        self.pushButton.setText(_translate("MainWindow", "Know The Weather"))
