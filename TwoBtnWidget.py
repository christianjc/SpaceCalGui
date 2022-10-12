# This Python file uses the following encoding: utf-8
from PySide6 import QtCore
from PySide6 import QtWidgets

from PySide6.QtCore import QObject
from PySide6.QtWidgets import (QWidget, QVBoxLayout, QPushButton, QFrame, QListView, QFormLayout,
                               QLabel, QHBoxLayout, QBoxLayout, QSizePolicy, QStyleOptionButton, QStyle)


class TwoBtnWidget(QtWidgets.QWidget):
    def __init__(self, stop="Off", start="On"):
        super().__init__()
        # Widgets
        self.stopBtn = QPushButton(stop)
        self.startBtn = QPushButton(start)
        # self.widget = QWidget()

        # Layouts
        self.mainLayout = QHBoxLayout(self)

        # Add Widgets
        self.mainLayout.insertWidget(0, self.stopBtn)
        self.mainLayout.insertWidget(1, self.startBtn)
