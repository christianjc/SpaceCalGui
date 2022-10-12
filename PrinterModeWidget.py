# This Python file uses the following encoding: utf-8
from PySide6 import QtWidgets

from PySide6.QtCore import (Signal)

from PySide6.QtWidgets import (QWidget, QVBoxLayout, QPushButton, QFrame, QFormLayout,
                               QLabel, QHBoxLayout, QSizePolicy, QStyleOptionButton, QStyle)


class PrinterModeWidget(QtWidgets.QWidget):
    modeChanged = Signal(bool)

    def __init__(self):
        super().__init__()

        # Widgets
        self.btnStop = QPushButton("Stop Printing")
        self.btnMode = QPushButton("On")
        self.lableMode = QLabel("Auto Printer Mode")
        self.modeWidget = QWidget()
        self.btnWidget = QWidget()

        # Widget properties
        self.btnStop.setDisabled(True)
        self.btnStop.hide()
        self.btnMode.setCheckable(True)
        self.btnMode.setChecked(True)

        # Layouts
        self.printerModeLayout = QHBoxLayout(self)
        self.toggleBtnLayout = QFormLayout(self.modeWidget)
        self.stopBtnLayout = QHBoxLayout(self.btnWidget)

        # insert Widgets
        self.toggleBtnLayout.addRow(self.lableMode, self.btnMode)
        self.stopBtnLayout.addWidget(self.btnStop)
        self.printerModeLayout.insertWidget(0, self.modeWidget)
        self.printerModeLayout.insertWidget(0, self.btnWidget)

        # Connect Signals
        self.btnMode.toggled.connect(self.setMode)

    def setMode(self):
        if self.btnMode.isChecked():
            self.btnStop.hide()
            self.isAutoPrintMode = True
            self.btnMode.setText(u"On")
        else:
            self.btnStop.show()
            self.isAutoPrintMode = False
            self.btnMode.setText(u"Off")
        self.modeChanged.emit(self.isAutoPrintMode)
