import sys
from PyQt5 import uic, QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QCheckBox, \
    QLabel, QInputDialog, QDialog, QFontComboBox, QPushButton, \
    QStackedWidget, QGridLayout, QFileDialog, QStyle, QStyleFactory
from PyQt5.QtCore import Qt
from uiFiles.MainWindow import Ui_MainWindow


class SPMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('uiFiles/MainWindow.ui', self)

        self.setWindowTitle('Анализ показателей стратегических документов субъекта РФ')
        self.show()
