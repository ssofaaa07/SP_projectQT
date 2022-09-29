import time

from PyQt5.QtCore import QThread

from classes.DataBase import DataBase
from classes.IndustriesIndicators import industries_indicators


class DBThreadInteraction(QThread):
    def __init__(self):
        super().__init__()
        self.main_window = None

        self.strategies = StrategiesThread()
        self.PM = PMThread()
        self.CYR = CYRThread()
        self.GP = GPThread()
        self.RP = RPThread()

        self.time_to_wait = 3600
        self.all_indicators_loaded = False

    def run(self) -> None:
        while True:
            if self.main_window is not None:
                self.main_window.updateDataInfoLabel.setText("Обновление информации из базы данных")
            self.all_indicators_loaded = False
            self.start_requests()

            if self.main_window is not None:
                self.main_window.updateDataInfoLabel.setText("Информация из базы данных обновлена")
            self.all_indicators_loaded = True
            self.sleep_timer()

    def start_requests(self):
        if self.main_window is not None:
            self.main_window.progressBar.setValue(0)

        print("Загрузка показателей стратегий")
        self.strategies.start()
        if self.main_window is not None:
            self.main_window.progressBar.setValue(20)

        print("Загрузка показателей ПМ")
        self.PM.start()
        if self.main_window is not None:
            self.main_window.progressBar.setValue(40)

        print("Загрузка показателей ЦУР")
        self.CYR.start()
        if self.main_window is not None:
            self.main_window.progressBar.setValue(60)

        print("Загрузка ГП показателей")
        self.GP.start()
        if self.main_window is not None:
            self.main_window.progressBar.setValue(80)

        print("Загрузка РП показателей")
        self.RP.start()
        if self.main_window is not None:
            self.main_window.progressBar.setValue(100)

        print("Всевозможные показатели загружены")

    def sleep_timer(self):
        remaining_time = self.time_to_wait
        while remaining_time > 0:
            time.sleep(1)
            remaining_time -= 1
            if self.main_window is not None:
                if remaining_time / 60 >= 1:
                    self.main_window.updateDataInfoLabel2.setText(
                        f"Автообновление через: {int(remaining_time / 60)} мин. "
                        f"{remaining_time - int(remaining_time / 60) * 60} сек."
                    )
                else:
                    self.main_window.updateDataInfoLabel2.setText(
                        f"Автообновление через: {remaining_time} сек."
                    )


class StrategiesThread(QThread):
    def __init__(self):
        super().__init__()
        self.DB = DataBase()

    def run(self) -> None:
        industries_indicators.indicators["Strategies"] = self.DB.get_strategy_indicators_names()


class PMThread(QThread):
    def __init__(self):
        super().__init__()
        self.DB = DataBase()

    def run(self) -> None:
        industries_indicators.indicators["PM"] = self.DB.get_PM_indicators_names()


class CYRThread(QThread):
    def __init__(self):
        super().__init__()
        self.DB = DataBase()

    def run(self) -> None:
        industries_indicators.indicators["CYR"] = self.DB.get_CYR_indicators_names()


class GPThread(QThread):
    def __init__(self):
        super().__init__()
        self.DB = DataBase()

    def run(self):
        industries_indicators.GP_industries_all = self.DB.get_industries()
        industries_indicators.GP_industries = industries_indicators.GP_industries_all[0]
        industries_indicators.GP_industries_ru = industries_indicators.GP_industries_all[1]

        self.__request_all_GP_indicators_by_industries__()

    def __request_all_GP_indicators_by_industries__(self):
        for industry in industries_indicators.GP_industries:
            indicators = self.DB.get_GP_indicators_names(industry)
            industries_indicators.indicators_by_industries[industry] = indicators


class RPThread(QThread):
    def __init__(self):
        super().__init__()
        self.DB = DataBase()

    def run(self):
        industries_indicators.RP_industries_all = self.DB.get_industries()
        industries_indicators.RP_industries = industries_indicators.RP_industries_all[0]
        industries_indicators.RP_industries_ru = industries_indicators.RP_industries_all[1]

        self.__request_all_RP_indicators_by_industries__()

    def __request_all_RP_indicators_by_industries__(self):
        for industry in industries_indicators.GP_industries:
            indicators = self.DB.get_RP_indicators_names(industry)
            industries_indicators.indicators_by_industries[industry] = indicators


DBInteraction = DBThreadInteraction()
