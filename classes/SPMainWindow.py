from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import Qt

from classes.SPAutoUpdateSettings import SPAutoUpdateSettings
from uiFiles.MainWindow import Ui_MainWindow
from classes.DataBase import DataBase


class SPMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, widget, widget_plus):
        super().__init__()
        # uic.loadUi('uiFiles/MainWindow.ui', self) # Подгрузка из ui файла
        self.setupUi(self)  # Подгрузка из py класса
        self.setWindowTitle('Анализ показателей стратегических документов субъекта РФ')
        self.DB = DataBase()

        self.indWidget = widget
        self.indWidget.main_window = self
        self.indWidgetPlus = widget_plus
        self.indWidgetPlus.main_window = self
        self.DBSettings = SPAutoUpdateSettings()

        self.first_selected_ind = ''
        self.second_selected_ind = ''

        self.connect_period_buttons_logic()
        self.connect_indicators_buttons_logic()
        self.connect_menubar_actions_logic()
        self.hide_period_periods()
        self.set_years()

        self.show()

    def connect_menubar_actions_logic(self):
        self.autoUpdateAction.triggered.connect(self.DBSettings.show)

    def change_info_text(self, widget_number, field_name, indicator_name, industry=None):
        if widget_number == 1:
            self.first_selected_ind = indicator_name
            print(widget_number, field_name, indicator_name, industry)
            self.firstIndicatorInfo.setText(
                "\n".join(["ПЕРВЫЙ ПОКАЗАТЕЛЬ", field_name, "", indicator_name])
                if industry is None else
                "\n".join(["ПЕРВЫЙ ПОКАЗАТЕЛЬ", field_name, industry, "", indicator_name])
            )
            self.firstIndicatorInfo.setWordWrap(True)
            self.firstIndicatorInfo.setAlignment(Qt.AlignCenter)
        elif widget_number == 2:
            self.second_selected_ind = indicator_name
            print(widget_number, field_name, indicator_name, industry)
            self.secondIndicatorInfo.setText(
                "\n".join(["ВТОРОЙ ПОКАЗАТЕЛЬ", field_name, "", indicator_name])
                if industry is None else
                "\n".join(["ВТОРОЙ ПОКАЗАТЕЛЬ", field_name, industry, "", indicator_name])
            )
            self.secondIndicatorInfo.setWordWrap(True)
            self.secondIndicatorInfo.setAlignment(Qt.AlignCenter)

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
        years = self.DB.get_years()

        self.oneYearComboBox.addItems(years)
        self.toComboBox.addItems(years)
        self.fromComboBox.addItems(years)
