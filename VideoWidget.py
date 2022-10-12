# This Python file uses the following encoding: utf-8
from PySide6 import QtCore
from PySide6 import QtWidgets

from PySide6.QtWidgets import (QWidget, QVBoxLayout, QPushButton, QFrame, QListView, QFormLayout,
                               QLabel, QHBoxLayout, QBoxLayout, QSizePolicy, QStyleOptionButton, QStyle)
from SelectBtnWidget import SelectBtnWidget
from TwoBtnWidget import TwoBtnWidget


class VideoWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        # Widgets
        self.videoWidget = QWidget()
        self.videoLabel = SelectBtnWidget(u"Video", u"No Video", u"Select...")
        self.videoBtns = TwoBtnWidget(u"Stop", u"Play")

        # Layouts
        self.videoLayout = QVBoxLayout(self.videoWidget)

        # Add Widgets to the Layouts
        self.videoLayout.insertWidget(0, self.videoLabel)
        self.videoLayout.insertWidget(1, self.videoBtns)
