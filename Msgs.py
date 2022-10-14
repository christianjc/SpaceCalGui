# This Python file uses the following encoding: utf-8
from PySide6 import QtCore
from PySide6 import QtWidgets

from PySide6.QtWidgets import (QWidget, QVBoxLayout, QPushButton, QFrame, QFormLayout, QMessageBox,
                               QLabel, QHBoxLayout, QSizePolicy, QStyleOptionButton, QStyle)


class Msgs(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.stopSysMsg = "Would you like stop the system?"
        self.endPrintMsg = "Would you like stop current print?"
        self.startPrintMsg = "Would you like begin printing?"
        self.msgBox = QMessageBox()
        self.msgBox.setStandardButtons(QMessageBox.No | QMessageBox.Yes)
        self.msgBox.setDefaultButton(QMessageBox.Yes)

    def confirmMsg(self, msg):
        # print(type(""), type(msg))
        assert type("") == type(msg), "wrong type"
        self.msgBox.setText(msg)
        return self.msgBox.exec()
