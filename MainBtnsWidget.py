# This Python file uses the following encoding: utf-8
from PySide6 import QtCore
from PySide6.QtCore import QSize, Slot
from PySide6 import QtWidgets
from PySide6.QtWidgets import (QWidget, QVBoxLayout, QPushButton, QFrame,
                               QLabel, QHBoxLayout, QSizePolicy, QStyleOptionButton, QStyle)


class MainBtnsWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # Widgets
        self.btnStop = QPushButton("Stop Printing")
        self.btnStart = QPushButton("Start Printing")

        # Set Widget properties
        self.btnStop.setProperty("StopBtn", True)
        self.btnStart.setProperty("StartBtn", True)
        self.btnStop.setDisabled(True)

        # Layouts
        self.mainBtnsLayout = QHBoxLayout(self)

        # Add widgets to layouts
        self.mainBtnsLayout.addWidget(self.btnStop)
        self.mainBtnsLayout.addWidget(self.btnStart)
        self.setStyleSheet(style)

    @Slot(bool)
    def setAutoPrintMode(self, mode):
        if mode == True:
            self.btnStop.setText(u"Stop Printing")
            self.btnStart.setText(u"Start Printing")
        else:
            self.btnStop.setText(u"End Print")
            self.btnStart.setText(u"Start Print")


##### Style Sheets ######

style = """
QPushButton {
border: 2px solid #8f8f91;
border-radius: 6px;
background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                  stop: 0 #f6f7fa, stop: 1 #dadbde);
min-width: 80px;
min-height: 80px;
}


QPushButton:pressed {
background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                  stop: 0 #dadbde, stop: 1 #f6f7fa);
}

QPushButton:flat {
border: none; /* no border for a flat push button */
}

QPushButton:default {
border-color: navy; /* make the default button prominent */
}


"""

# QPushButton[isActive="false"] {
# background-color: gray;
# }
