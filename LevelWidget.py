# This Python file uses the following encoding: utf-8
from PySide6 import QtCore
from PySide6 import QtWidgets
from PySide6.QtWidgets import (QWidget, QVBoxLayout, QPushButton, QFrame,
                               QLabel, QHBoxLayout, QSizePolicy, QStyleOptionButton, QStyle)
from SelectBtnWidget import SelectBtnWidget


class LevelWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # Widget
        self.levelSelect = SelectBtnWidget(u"Level", u"5", u"Select...")
