# This Python file uses the following encoding: utf-8
import imp
from PySide6 import QtCore
from PySide6 import QtWidgets
from PySide6.QtCore import QObject
from PySide6.QtWidgets import (QWidget, QVBoxLayout, QPushButton, QFrame, QListView, QFormLayout,
                               QLabel, QHBoxLayout, QBoxLayout, QSizePolicy, QStyleOptionButton, QStyle)

from SelectBtnWidget import SelectBtnWidget
from DisplayField import DisplayField
from TwoBtnWidget import TwoBtnWidget


class PrinterWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # Widgets
        self.powerWidget = QWidget()
        self.powerLabel = DisplayField(u"Power:", u"Off")
        self.powerBtns = TwoBtnWidget(u"Off", u"On")
        self.ledWidget = QWidget()
        self.ledLabel = DisplayField(u"Led:", u"Off")
        self.ledBtns = TwoBtnWidget(u"Off", u"On")
        self.motorWidget = QWidget()
        self.motorLabel = SelectBtnWidget(
            u"Vial Motor Speed:", u"0", u"Change Speed")
        self.motorBtns = TwoBtnWidget(u"Stop", u"Run")

        self.selectPrinterWidget = SelectBtnWidget(u"Printer:", u"All")

        # Layouts
        self.powerLayout = QVBoxLayout(self.powerWidget)
        self.ledLayout = QVBoxLayout(self.ledWidget)
        self.motorLayout = QVBoxLayout(self.motorWidget)

        # Add Widgets to layouts
        self.powerLayout.insertWidget(0, self.powerLabel)
        self.powerLayout.insertWidget(1, self.powerBtns)
        self.ledLayout.insertWidget(0, self.ledLabel)
        self.ledLayout.insertWidget(1, self.ledBtns)
        self.motorLayout.insertWidget(0, self.motorLabel)
        self.motorLayout.insertWidget(1, self.motorBtns)
