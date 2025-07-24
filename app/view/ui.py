from PyQt5 import QtCore, QtGui, QtWidgets
from .res_rc import *


class Ui(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setFixedSize(800, 600)
        Form.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0  rgb(26, 26, 26), stop:1 rgb(23, 23, 23));")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(0, 0, 791, 591))
        self.widget.setStyleSheet("QPushButton {\n"
                                  "    font: 75 12pt \"JetBrainsMonoNL Nerd Font\";\n"
                                  "    border-radius: 10px;\n"
                                  "    border-color: rgb(0, 0, 0);\n"
                                  "    background-color: rgb(68, 68, 68);\n"
                                  "    color: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QPushButton:hover {\n"
                                  "    background-color: rgb(33, 39, 45);\n"
                                  "}")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(10, 0, 781, 591))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QtCore.QSize(800, 600))
        self.label.setStyleSheet("border-image: url(:/images/images/background.jpg);\n"
                                 "border-radius: 20px;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(280, 30, 261, 51))
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "font: 75 36pt \"JetBrainsMonoNL Nerd Font\";")
        self.label_2.setObjectName("label_2")
        self.Start = QtWidgets.QPushButton(self.widget)
        self.Start.setGeometry(QtCore.QRect(540, 510, 171, 51))
        self.Start.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Start.setStyleSheet("")
        self.Start.setObjectName("Start")
        self.Output = QtWidgets.QLabel(self.widget)
        self.Output.setGeometry(QtCore.QRect(90, 90, 621, 411))
        self.Output.setStyleSheet("background-color: rgba(0, 0, 0, 100);\n"
                                  "border-radius: 10px;\n"
                                  "font: 75 8pt \"JetBrainsMonoNL Nerd Font\";\n"
                                  "color: rgb(255, 255, 255);")
        self.Output.setText("")
        self.Output.setObjectName("Output")
        self.Path = QtWidgets.QPushButton(self.widget)
        self.Path.setGeometry(QtCore.QRect(90, 510, 171, 51))
        self.Path.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Path.setStyleSheet("")
        self.Path.setObjectName("Path")
        self.Conf = QtWidgets.QPushButton(self.widget)
        self.Conf.setGeometry(QtCore.QRect(320, 510, 171, 51))
        self.Conf.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Conf.setStyleSheet("")
        self.Conf.setObjectName("Conf")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "AI Parser"))
        self.Start.setText(_translate("Form", "Start"))
        self.Path.setText(_translate("Form", "Path to file"))
        self.Conf.setText(_translate("Form", "Set config"))
