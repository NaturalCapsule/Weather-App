from PyQt6 import QtCore, QtGui, QtWidgets
from qfluentwidgets import FluentWindow, PushButton
import httpx
import os
from PyQt6.QtGui import QPixmap, QIcon
from time import strftime, localtime
from PyQt6.QtCore import Qt, QTimer
from io import BytesIO
from datetime import datetime
from get_weather_info import WeatherInfo


class Ui_MainWindow(object):

    def __init__(self, MainWindow):
        self.MainWindow = MainWindow



    def on_pushButton_clicked(self):
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1)
        self.now = localtime()
        self.hour = self.now.tm_hour
        self.minute = self.now.tm_min

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
        self.display_sunset = data['weather'][0]['astronomy'][0]['sunset']
        self.display_sunrise = data['weather'][0]['astronomy'][0]['sunrise']
        self.sunset_time = datetime.strptime(self.display_sunset, "%I:%M %p")
        self.sunrise_time = datetime.strptime(self.display_sunrise, "%I:%M %p")
        self.sunset_hour = self.sunset_time.hour
        self.sunset_min = self.sunset_time.minute
        self.sunrise_hour = self.sunrise_time.hour
        self.sunrise_min = self.sunrise_time.minute
        self.sunset_minutes = self.sunset_hour * 60 + self.sunset_min
        self.sunrise_minutes = self.sunrise_hour * 60 + self.sunrise_min
        self.current_minutes = self.hour * 60 + self.minute

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
        self.label_2.setText("Time")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        if self.hour < 12:
            self.p_hour = "AM"
        else:
            self.p_hour = "PM"

        if self.sunset_hour > 12:
            self.p_sunset_hour = "PM"

        if self.current_minutes >= self.sunset_minutes or self.current_minutes < self.sunrise_minutes:
            self.MainWindow.setStyleSheet("background-color: black;")
            self.label_5.setPixmap(QPixmap(u'assets/moon.png'))

        else:
            self.label_5.setPixmap(QPixmap(u'assets/sun.png'))
        

    def setupUi(self):

        # self.timer = QTimer()
        # self.timer.timeout.connect(self.update_time)
        # self.timer.start(1)

        self.MainWindow.setObjectName("MainWindow")
        self.MainWindow.resize(590, 397)
        self.icon_path = os.path.abspath("assets/weather-app.ico")
        self.MainWindow.setWindowIcon(QIcon(self.icon_path))
        self.centralwidget = QtWidgets.QWidget(parent=self.MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.frame_3 = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_7.setObjectName("gridLayout_7")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_7.addItem(spacerItem, 0, 3, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_7.addItem(spacerItem1, 2, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(51, 78, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_7.addItem(spacerItem2, 2, 4, 2, 1)
        self.label_2 = QtWidgets.QLabel(parent=self.frame_3)
        self.label_2.setStyleSheet("QLabel {\n"
"        color: black;\n"
"        background-color: white;\n"
"        border-radius: 10px;\n"
"        padding: 10px;\n"
"        font-size: 18px;\n"
"        font-weight: bold;\n"
"        font-family: Arial;\n"
"    }")
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.gridLayout_7.addWidget(self.label_2, 2, 3, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(51, 78, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_7.addItem(spacerItem3, 2, 2, 2, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_7.addItem(spacerItem4, 2, 5, 1, 1)
        self.label_6 = QtWidgets.QLabel(parent=self.frame_3)
        self.label_6.setStyleSheet("QLabel {\n"
"        color: black;\n"
"        background-color: white;\n"
"        border-radius: 10px;\n"
"        padding: 10px;\n"
"        font-size: 18px;\n"
"        font-weight: bold;\n"
"        font-family: Arial;\n"
"    }")
        self.label_6.setText("")
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.gridLayout_7.addWidget(self.label_6, 3, 3, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_7.addItem(spacerItem5, 4, 3, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_7.addItem(spacerItem6, 1, 2, 1, 1)
        self.gridLayout_6.addWidget(self.frame_3, 0, 3, 1, 1)
        self.frame_4 = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_8.setObjectName("gridLayout_8")
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_8.addItem(spacerItem7, 2, 5, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_8.addItem(spacerItem8, 0, 2, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_8.addItem(spacerItem9, 2, 1, 2, 1)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_8.addItem(spacerItem10, 2, 0, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_8.addItem(spacerItem11, 2, 4, 2, 1)
        self.label = QtWidgets.QLabel(parent=self.frame_4)
        self.label.setEnabled(True)
        self.label.setMouseTracking(False)
        self.label.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label.setText("")
        self.label.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.gridLayout_8.addWidget(self.label, 2, 2, 1, 1)
        self.label_1 = QtWidgets.QLabel(parent=self.frame_4)
        self.label_1.setStyleSheet("QLabel {\n"
"        color: black;\n"
"        background-color: white;\n"
"        border-radius: 10px;\n"
"        padding: 10px;\n"
"        font-size: 18px;\n"
"        font-weight: bold;\n"
"        font-family: Arial;\n"
"    }")
        self.label_1.setText("")
        self.label_1.setObjectName("label_1")
        self.gridLayout_8.addWidget(self.label_1, 3, 2, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_8.addItem(spacerItem12, 4, 2, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_8.addItem(spacerItem13, 1, 1, 1, 1)
        self.gridLayout_6.addWidget(self.frame_4, 0, 1, 1, 1)
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem14 = QtWidgets.QSpacerItem(145, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_3.addItem(spacerItem14, 2, 2, 1, 1)
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
        spacerItem15 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_3.addItem(spacerItem15, 0, 2, 1, 1)
        spacerItem16 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_3.addItem(spacerItem16, 1, 3, 1, 1)
        spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_3.addItem(spacerItem17, 1, 0, 1, 1)
        spacerItem18 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_3.addItem(spacerItem18, 1, 1, 1, 1)
        spacerItem19 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_3.addItem(spacerItem19, 1, 4, 1, 1)
        self.gridLayout_6.addWidget(self.frame, 1, 0, 1, 4)
        self.frame_2 = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_3 = QtWidgets.QLabel(parent=self.frame_2)
        self.label_3.setObjectName("label_3")
        self.gridLayout_5.addWidget(self.label_3, 2, 2, 1, 1)
        spacerItem20 = QtWidgets.QSpacerItem(51, 88, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_5.addItem(spacerItem20, 2, 3, 2, 1)
        spacerItem21 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_5.addItem(spacerItem21, 2, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(parent=self.frame_2)
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.gridLayout_5.addWidget(self.label_5, 0, 0, 1, 2)
        spacerItem22 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_5.addItem(spacerItem22, 4, 2, 1, 1)
        spacerItem23 = QtWidgets.QSpacerItem(51, 88, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_5.addItem(spacerItem23, 2, 1, 2, 1)
        spacerItem24 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_5.addItem(spacerItem24, 0, 2, 1, 1)
        spacerItem25 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_5.addItem(spacerItem25, 2, 4, 1, 1)
        self.label_4 = QtWidgets.QLabel(parent=self.frame_2)
        self.label_4.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label_4.setStyleSheet("QLabel {\n"
"        color: black;\n"
"        background-color: white;\n"
"        border-radius: 10px;\n"
"        padding: 10px;\n"
"        font-size: 18px;\n"
"        font-weight: bold;\n"
"        font-family: Arial;\n"
"    }")
        self.label_4.setText("")
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.gridLayout_5.addWidget(self.label_4, 3, 2, 1, 1)
        spacerItem26 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_5.addItem(spacerItem26, 1, 1, 1, 1)
        self.gridLayout_6.addWidget(self.frame_2, 0, 0, 1, 1)
        self.MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(self.MainWindow)
        QtCore.QMetaObject.connectSlotsByName(self.MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Know The Weather"))

    def update_time(self):
        self.label_6.setText(strftime('%H:%M:%S'))
