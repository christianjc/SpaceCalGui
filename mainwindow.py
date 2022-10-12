# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)

from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
                               QLayout, QMainWindow, QPushButton, QSizePolicy,
                               QStatusBar, QTabWidget, QVBoxLayout, QWidget)

from HomePageWidget import HomePageWidget
from PrinterPageWidget import PrinterPageWidget


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.resize(800, 600)

        # Widgets
        self.tabWidget = QTabWidget()
        self.homePage = HomePageWidget()
        self.printPage = PrinterPageWidget()

        # Editing Widgits
        self.tabWidget.setDocumentMode(True)

        # Layouts
        self.mainLayout = QVBoxLayout(self.tabWidget)

        # Inserting widget tabs
        self.tabWidget.insertTab(0,self.homePage, "Home")
        self.tabWidget.insertTab(1,self.printPage, "Printer Controller")

        # Setting the central widget for the main window to be the tabWidget
        self.setCentralWidget(self.tabWidget)


        # Define the size policy for the tab widgit -- we want the minimum to be 700 by 500
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
#        self.setSizePolicy(sizePolicy)




if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
