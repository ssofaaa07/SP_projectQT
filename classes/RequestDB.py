from PyQt5.QtCore import QThread
from classes.DataBase import DataBase


class RequestDB(QThread):
    def __init__(self, main_window, schema_name):
        super().__init__()
        self.DB = DataBase()

        self.main_window = main_window
        self.indicators = []
        self.schema_name = schema_name

    def run(self) -> None:
        self.main_window.allIndicatorsListWidget.clear()
        self.main_window.allIndicatorsListWidget.addItem("Загрузка показателей")

        match self.schema_name:
            case "Strategies":
                self.indicators = self.DB.get_strategy_indicators_names()
            case "PM":
                self.indicators = self.DB.get_PM_indicators_names()
            case "CYR":
                self.indicators = self.DB.get_CYR_indicators_names()

        self.main_window.indicator_list = self.indicators

        self.main_window.allIndicatorsListWidget.clear()
        self.main_window.allIndicatorsListWidget.addItems(self.indicators)


class RequestDBPlus(QThread):
    def __init__(self, main_window, schema_name):
        super().__init__()
        self.DB = DataBase()
        self.main_window = main_window

        self.indicators = []
        self.schema_name = schema_name

        self.GP_industries_all = None
        self.GP_industries = None
        self.GP_industries_ru = None

        self.RP_industries_all = None
        self.RP_industries = None
        self.RP_industries_ru = None

        self.RBDPIndustries = RequestDBPlusIndustries(self)
        self.RBDPIndustries.start()

    def run(self) -> None:
        self.main_window.allIndicatorsListWidget.clear()
        self.main_window.allIndicatorsListWidget.addItem("Загрузка показателей")

        industry_index = self.main_window.chooseIndusrtyComboBox.currentIndex()
        match self.schema_name:
            case "GP":
                self.indicators = self.DB.get_GP_indicators_names(self.GP_industries[industry_index])
            case "RP":
                # ОЖИДАНИЕ ГОТОВЫХ РЕГИОНАЛЬНЫХ ПРОЕКТОВ
                self.indicators = self.DB.get_RP_indicators_names(self.RP_industries[industry_index])

        self.main_window.indicator_list = self.indicators

        self.main_window.allIndicatorsListWidget.clear()
        self.main_window.allIndicatorsListWidget.addItems(self.indicators)


class RequestDBPlusIndustries(QThread):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window

    def run(self) -> None:
        if self.main_window.GP_industries_all is None:
            self.main_window.GP_industries_all = self.main_window.DB.get_industries()
            self.main_window.GP_industries = self.main_window.GP_industries_all[0]
            self.main_window.GP_industries_ru = self.main_window.GP_industries_all[1]
            self.main_window.main_window.chooseIndustryComboBox.addItems(self.main_window.GP_industries_ru)

        if self.main_window.RP_industries_all is None:
            self.main_window.RP_industries_all = self.main_window.DB.get_industries()
            self.main_window.RP_industries = self.main_window.RP_industries_all[0]
            self.main_window.RP_industries_ru = self.main_window.RP_industries_all[1]
            self.main_window.main_window.chooseIndustryComboBox.addItems(self.main_window.RP_industries_ru)
