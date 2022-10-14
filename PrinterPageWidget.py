# This Python file uses the following encoding: utf-8
from LevelWidget import LevelWidget
from PySide6 import QtCore
from PySide6 import QtWidgets
from PySide6.QtWidgets import (QWidget, QVBoxLayout, QPushButton)
from PySide6.QtWidgets import (QWidget, QVBoxLayout, QPushButton, QFrame, QListView, QFormLayout,
                               QLabel, QHBoxLayout, QBoxLayout, QSizePolicy, QStyleOptionButton, QStyle)

from PrinterWidget import PrinterWidget
from SelectBtnWidget import SelectBtnWidget
from TwoBtnWidget import TwoBtnWidget
from VideoWidget import VideoWidget


class PrinterPageWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # Widgets
        self.printerWidget = PrinterWidget()
        self.videoWidget = VideoWidget()
        self.levelWidget = LevelWidget()
        self.mainBtns = TwoBtnWidget(u"Stop", u"Print")

        # Widget properties
        # self.printerWidget.powerWidget.setStyleSheet("border-style: outset;"
        #                                              "border-width: 2px;"
        #                                              "border-radius: 10px;"
        #                                              "border-color: beige;"
        #                                              "font: bold 14px;"
        #                                              "min-width: 10em;"
        #                                              "padding: 6px;")

        # Layouts
        self.hLayouts = [QHBoxLayout] * 4
        self.verticalLayout = QVBoxLayout(self)
        for i in range(4):
            self.hLayouts[i] = QHBoxLayout()

        # Add widgets to Layouts
        self.hLayouts[0].insertWidget(0, self.printerWidget.powerWidget)
        self.hLayouts[0].insertWidget(
            1, self.printerWidget.selectPrinterWidget)
        self.hLayouts[1].insertWidget(0, self.printerWidget.ledWidget)
        self.hLayouts[1].insertWidget(1, self.levelWidget.levelSelect)
        self.hLayouts[2].insertWidget(0, self.videoWidget.videoWidget)
        self.hLayouts[2].insertWidget(1, self.printerWidget.motorWidget)
        self.hLayouts[3].insertWidget(0, self.mainBtns)

        for i in range(4):
            self.verticalLayout.insertLayout(i, self.hLayouts[i])

        # Signals and Slots
        self.printerWidget.btnPressed.connect(self.printSignals)

    def printSignals(self, sig):
        print(sig)
