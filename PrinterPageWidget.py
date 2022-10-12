# This Python file uses the following encoding: utf-8
from PySide6 import QtCore
from PySide6 import QtWidgets
from PySide6.QtWidgets import (QWidget, QVBoxLayout, QPushButton)
from PySide6.QtWidgets import (QWidget, QVBoxLayout, QPushButton, QFrame, QListView, QFormLayout,
                               QLabel, QHBoxLayout, QBoxLayout, QSizePolicy, QStyleOptionButton, QStyle)

from PrinterWidget import PrinterWidget
from SelectBtnWidget import SelectBtnWidget
from VideoWidget import VideoWidget


class PrinterPageWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # Widgets
        self.printerWidget = PrinterWidget()
        self.videoWidget = VideoWidget()
        self.button = SelectBtnWidget(u"Video:", u"No Video", u"Select...")
        self.button_2 = SelectBtnWidget(u"Video:", u"No Video", u"Select...")

        # Layouts
        self.printerPageLayout = QVBoxLayout(self)

        # Add widgets to Layouts
        self.printerPageLayout.insertWidget(0, self.printerWidget.powerWidget)
        self.printerPageLayout.insertWidget(1, self.printerWidget.ledWidget)
        self.printerPageLayout.insertWidget(2, self.printerWidget.motorWidget)
        self.printerPageLayout.insertWidget(2, self.videoWidget.videoWidget)
