# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'second_sweeper_design.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(420, 570)
        self.time_lcd = QtWidgets.QLCDNumber(Form)
        self.time_lcd.setGeometry(QtCore.QRect(2, 0, 171, 70))
        self.time_lcd.setMode(QtWidgets.QLCDNumber.Dec)
        self.time_lcd.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.time_lcd.setObjectName("time_lcd_2")
        self.smile_button = QtWidgets.QPushButton(Form)
        self.smile_button.setGeometry(QtCore.QRect(172, 0, 70, 70))
        self.smile_button.setObjectName("smile_button_2")
        self.is_dig = QtWidgets.QRadioButton(Form)
        self.is_dig.setGeometry(QtCore.QRect(47, 515, 100, 30))
        self.is_dig.setObjectName("is_dig_2")
        self.is_flag = QtWidgets.QRadioButton(Form)
        self.is_flag.setGeometry(QtCore.QRect(207, 515, 200, 30))
        self.is_flag.setObjectName("is_flag_2")
        self.bombs_lcd = QtWidgets.QLCDNumber(Form)
        self.bombs_lcd.setGeometry(QtCore.QRect(240, 0, 180, 70))
        self.bombs_lcd.setMode(QtWidgets.QLCDNumber.Dec)
        self.bombs_lcd.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.bombs_lcd.setObjectName("bombs_lcd_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.smile_button.setText(_translate("Form", "PushButton"))
        self.is_dig.setText(_translate("Form", "Копать"))
        self.is_flag.setText(_translate("Form", "Поставить флаг"))
