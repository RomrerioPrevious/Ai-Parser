import os
import re

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog

from .. import FileHandler
from ..config import CONFIG
from .res_rc import *


class Ui(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 600)
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
        self.Output.setAlignment(QtCore.Qt.AlignTop)
        self.Output.setGeometry(QtCore.QRect(90, 90, 621, 411))
        self.Output.setStyleSheet("background-color: rgba(0, 0, 0, 100);\n"
                                  "border-radius: 10px;\n"
                                  "font: 75 10pt \"JetBrainsMonoNL Nerd Font\";\n"
                                  "color: rgb(255, 255, 255);")
        self.Output.setText("")
        self.Output.setObjectName("Output")
        self.Path = QtWidgets.QPushButton(self.widget)
        self.Path.setGeometry(QtCore.QRect(90, 510, 171, 51))
        self.Path.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Path.setStyleSheet("")
        self.Path.setObjectName("Path")
        self.Conf = QtWidgets.QPushButton(self.widget)
        self.Conf.setGeometry(QtCore.QRect(310, 510, 181, 51))
        self.Conf.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Conf.setStyleSheet("")
        self.Conf.setObjectName("Conf")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("AI Parser", "AI Parser"))
        Form.setWindowIcon(QtGui.QIcon(":/images/images/icon.png"))
        self.label_2.setText(_translate("Form", "AI Parser"))
        self.Start.setText(_translate("Form", "Start"))
        self.Path.setText(_translate("Form", "Path to file"))
        self.Conf.setText(_translate("Form", "Set config"))

        self.Start.clicked.connect(lambda: self.on_Start_clicked(Form))
        self.Path.clicked.connect(lambda: self.on_Path_clicked(Form))
        self.Conf.clicked.connect(lambda: self.on_Conf_clicked(Form))

    def on_Start_clicked(self, Form):
        try:
            handler = FileHandler()
            for log in handler.parse():
                if log[1]:
                    break
                else:
                    print(log[0])
                    self.Output.setText(log[0])
        except Exception as e:
            self.Output.setText(f"Error: {e}")


    def on_Path_clicked(self, Form):
        file_path, _ = QFileDialog.getOpenFileName(
            Form,
            "Выберите файл",
            "",
            "Excel Files (*.xlsx *.xls)"
        )
        if not file_path:
            self.Output.setText(f"Error: the file path has not been entered.")
            return
        CONFIG.app.path_to_file = file_path
        with open("resources/config.toml", "r", encoding="utf-8") as file:
            data = file.read()
            pattern = r'(path_to_file\s*=\s*)([\'"]?)(.*?)\2'

            updated_data = re.sub(
                pattern,
                lambda
                    m: f"{m.group(1)}{m.group(2) if m.group(2) else ''}{file_path}{m.group(2) if m.group(2) else ''}",
                data,
                flags=re.IGNORECASE
            )
        with open("resources/config.toml", "w", encoding="utf-8") as file:
            file.write(updated_data)
        self.Output.setText(f"Current path: {file_path}")

    def on_Conf_clicked(self, Form):
        project_root = os.getcwd()
        os.startfile(f"{project_root}/resources/config.toml")
