import sys
from PyQt5 import uic, QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QCheckBox, \
    QLabel, QInputDialog, QDialog, QFontComboBox, QPushButton, \
    QStackedWidget, QGridLayout, QFileDialog, QStyle, QStyleFactory
from PyQt5.QtCore import Qt
from uiFiles.MainWindow import Ui_MainWindow
from uiFiles.IndSubMenuWidget import Ui_Form as IndWidget
from uiFiles.IndSubMenuWidget1 import Ui_Form as IndWidgetPlus
from classes.DataBase import DB
import time


class SPMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        # uic.loadUi('uiFiles/MainWindow.ui', self) # Подгрузка из ui файла
        self.setupUi(self)  # Подгрузка из py класса
        self.setWindowTitle('Анализ показателей стратегических документов субъекта РФ')

        self.indWidget = SPIndWidget()
        self.indWidgetPlus = SPIndWidgetPlus()

        self.connect_period_buttons_logic()
        self.connect_indicators_buttons_logic()
        self.hide_period_periods()
        self.set_years()

        self.show()

    def connect_period_buttons_logic(self) -> None:
        self.oneYearButton.clicked.connect(self.hide_period_periods)
        self.yearPeriodButton.clicked.connect(self.hide_period_one_year)
        self.set_years()

    def connect_indicators_buttons_logic(self) -> None:
        self.CYRPushButton.clicked.connect(self.indWidget.showCYRWidget)
        self.PMPushButton.clicked.connect(self.indWidget.showPMWidget)
        self.strategyPushButton.clicked.connect(self.indWidget.showStrategyWidget)
        self.CYRPushButton2.clicked.connect(self.indWidget.showCYRWidget)
        self.PMPushButton2.clicked.connect(self.indWidget.showPMWidget)
        self.strategyPushButton2.clicked.connect(self.indWidget.showStrategyWidget)

        self.GPPushButton.clicked.connect(self.indWidgetPlus.showGPWidget)
        self.RPPushButton.clicked.connect(self.indWidgetPlus.showRPWidget)
        self.GPPushButton2.clicked.connect(self.indWidgetPlus.showGPWidget)
        self.RPPushButton2.clicked.connect(self.indWidgetPlus.showRPWidget)

    def hide_period_periods(self) -> None:
        self.yearPeriodButton.setDisabled(False)
        self.oneYearComboBox.show()

        self.fromComboBox.hide()
        self.fromLabel.hide()
        self.toComboBox.hide()
        self.toLabel.hide()
        self.oneYearButton.setDisabled(True)

    def hide_period_one_year(self) -> None:
        self.oneYearButton.setDisabled(False)
        self.oneYearComboBox.hide()

        self.fromComboBox.show()
        self.fromLabel.show()
        self.toComboBox.show()
        self.toLabel.show()
        self.yearPeriodButton.setDisabled(True)

    def set_years(self) -> None:
        years = DB.get_years()

        self.oneYearComboBox.addItems(years)
        self.toComboBox.addItems(years)
        self.fromComboBox.addItems(years)


class SPIndWidget(QDialog, IndWidget):
    def __init__(self):
        super().__init__()
        # uic.loadUi('uiFiles/IndSubMenuWidget.ui', self) # Подгрузка из ui файла
        self.setupUi(self)  # Подгрузка из py класса

        self.new_ind_list = []
        self.indicator_list = []
        self.accepted_indicator = ''
        self.full_list_active = True

        self.textEdit.textChanged.connect(self.find_similiar_indicator)
        self.buttonBox.accepted.connect(self.accept_indicator)

    def find_similiar_indicator(self):
        text = self.textEdit.toPlainText()
        if len(text) > 0:
            self.new_ind_list = [indicator for indicator in self.indicator_list if text.lower() in indicator.lower()]
            self.listWidget.clear()
            self.listWidget.addItems(self.new_ind_list)
            self.full_list_active = False
        else:
            self.listWidget.clear()
            self.listWidget.addItems(self.indicator_list)
            self.full_list_active = True

    def accept_indicator(self):
        row_number = self.listWidget.currentRow()
        if self.full_list_active:
            self.accepted_indicator = self.indicator_list[row_number]
        else:
            self.accepted_indicator = self.new_ind_list[row_number]
        self.hide()
        print(self.accepted_indicator)

    def showCYRWidget(self, ind_type) -> None:
        self.setWindowTitle(f'Выбор показателей ЦУР')
        self.show()

    def showStrategyWidget(self) -> None:
        self.setWindowTitle(f'Выбор показателей Стратегии развития')
        self.indicator_list = DB.get_indicator_names_by_schema('Strategies')
        self.listWidget.addItems(self.indicator_list)

        self.show()

    def showPMWidget(self) -> None:
        self.setWindowTitle(f'Выбор показателей Плана мероприятий')
        ind_names = DB.get_indicator_names_by_schema('public')
        self.listWidget.addItems(ind_names)

        self.show()


class SPIndWidgetPlus(QDialog, IndWidgetPlus):
    def __init__(self):
        super().__init__()
        # uic.loadUi('uiFiles/IndSubMenuWidget.ui', self) # Подгрузка из ui файла
        self.setupUi(self)  # Подгрузка из py класса

    def showGPWidget(self, ind_type) -> None:
        self.setWindowTitle(f'Выбор показателей Государственных проектов')
        self.show()

    def showRPWidget(self) -> None:
        self.setWindowTitle(f'Выбор показателей Региональных проектов')
        self.show()
