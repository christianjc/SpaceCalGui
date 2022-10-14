# This Python file uses the following encoding: utf-8
import imp
from PySide6 import QtCore
from PySide6 import QtWidgets
from PySide6.QtCore import QObject, Signal, Slot
from PySide6.QtWidgets import (QWidget, QVBoxLayout, QPushButton, QFrame, QListView, QFormLayout, QInputDialog,
                               QLabel, QHBoxLayout, QBoxLayout, QSizePolicy, QStyleOptionButton, QStyle)

from SelectBtnWidget import SelectBtnWidget
from DisplayField import DisplayField
from TwoBtnWidget import TwoBtnWidget


class PrinterWidget(QtWidgets.QWidget):
    btnPressed = Signal(str)

    def __init__(self):
        super().__init__()

        ####### Widgets ########
        # PowerWidget
        self.powerWidget = QWidget()
        self.powerLabel = DisplayField(u"Power:", u"Off")
        self.powerBtns = TwoBtnWidget(u"Off", u"On")
        # LedWidget
        self.ledWidget = QWidget()
        self.ledLabel = DisplayField(u"Led:", u"Off")
        self.ledBtns = TwoBtnWidget(u"Off", u"On")
        # Vial MotorWidget
        self.motorWidget = QWidget()
        self.motorLabel = SelectBtnWidget(
            u"Vial Motor Speed:", u"0", u"Change Speed")
        self.motorBtns = TwoBtnWidget(u"Stop", u"Run")
        # SelectPrinterWidget
        self.selectPrinterWidget = SelectBtnWidget(
            u"Printer:", u"All", u"Select...")

        ###### Layouts #########
        self.powerLayout = QVBoxLayout(self.powerWidget)
        self.ledLayout = QVBoxLayout(self.ledWidget)
        self.motorLayout = QVBoxLayout(self.motorWidget)

        ####### Add Widgets to layouts #########
        self.powerLayout.insertWidget(0, self.powerLabel)
        self.powerLayout.insertWidget(1, self.powerBtns)
        self.ledLayout.insertWidget(0, self.ledLabel)
        self.ledLayout.insertWidget(1, self.ledBtns)
        self.motorLayout.insertWidget(0, self.motorLabel)
        self.motorLayout.insertWidget(1, self.motorBtns)

        ######### Signals and Slots ##########
        # Power Buttons
        self.powerBtns.startBtn.clicked.connect(self.powerBtnStartPressed)
        self.powerBtns.stopBtn.clicked.connect(self.powerBtnStopPressed)
        # Led Buttons
        self.ledBtns.startBtn.clicked.connect(self.ledBtnsStartPressed)
        self.ledBtns.stopBtn.clicked.connect(self.ledBtnsStopPressed)
        # Vial Motor Buttons
        self.motorBtns.startBtn.clicked.connect(self.motorBtnsStartPressed)
        self.motorBtns.stopBtn.clicked.connect(self.motorBtnsStopPressed)
        self.motorLabel.btnSelect.clicked.connect(self.motorSelectBtnPressed)
        # Select Printer Buttons
        self.selectPrinterWidget.btnSelect.clicked.connect(
            self.selectPrinterBtnPressed)

    def powerBtnStartPressed(self):
        printer = self.getCurrPrinter()
        self.btnPressed.emit("proj-on-" + printer.lower())

    def powerBtnStopPressed(self):
        printer = self.getCurrPrinter()
        self.btnPressed.emit("proj-off-" + printer.lower())

    def ledBtnsStartPressed(self):
        printer = self.getCurrPrinter()
        self.btnPressed.emit("proj-led-on-" + printer.lower())

    def ledBtnsStopPressed(self):
        printer = self.getCurrPrinter()
        self.btnPressed.emit("proj-led-off-" + printer)

    def motorBtnsStartPressed(self):
        speed = self.getCurrMotorSpeed()
        printer = self.getCurrPrinter()
        self.btnPressed.emit("motor-on-" + speed + "-" + printer)

    def motorBtnsStopPressed(self):
        printer = self.getCurrPrinter()
        self.btnPressed.emit("motor-off-" + printer)

    def motorSelectBtnPressed(self):
        items = ["0", "10", "15", "20", "25", "30"]
        item, ok = QInputDialog.getItem(self, "QInputDialog::getItem()",
                                        "Season:", items, 0, False)
        if ok and item:
            self.motorLabel.display.field.setText(item)

    def selectPrinterBtnPressed(self):
        items = ["All", "1", "2", "3", "4", "5"]
        item, ok = QInputDialog.getItem(self, "Select A Printer",
                                        "Please select a printer", items, 0, False)
        if ok and item:
            self.selectPrinterWidget.display.field.setText(item)

    def getCurrPrinter(self):
        return self.selectPrinterWidget.display.field.text()

    def getCurrMotorSpeed(self):
        return self.motorLabel.display.field.text()
