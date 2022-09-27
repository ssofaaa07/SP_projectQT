import logging

from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox, QLabel
from uiFiles.IndSubMenuWidget import Ui_Form as IndWidget
from classes.IndustriesIndicators import industries_indicators
from classes.DBThreadInteraction import DBInteraction


class SPIndWidget(QDialog, IndWidget):
    def __init__(self):
        super().__init__()
        # uic.loadUi('uiFiles/IndSubMenuWidget.ui', self) # Подгрузка из ui файла
        self.setupUi(self)  # Подгрузка из py класса
        self.main_window = None

        self.message_box = QLabel("Загрузка показателей...")
        self.message_box.setWindowTitle("Подключение к базе данных")

        self.indicator_list = []
        self.search_ind_list = []
        self.last_used_indicators = []
        self.recommended_indicators = []

        self.accepted_indicator = ''

        self.full_list_active = True
        self.indicator_number = None
        self.field_name = ""

        self.connect_all_list_widgets_logic()
        self.searchIndicatorsTextEdit.textChanged.connect(self.find_similar_indicator)
        self.buttonBox.accepted.connect(self.accept_indicator)

    def connect_all_list_widgets_logic(self) -> None:
        self.allIndicatorsListWidget.itemSelectionChanged.connect(self.item_changed)
        self.recommendsListWidget.itemSelectionChanged.connect(self.item_changed)
        self.lastSearchedListWidget.itemSelectionChanged.connect(self.item_changed)

    def item_changed(self) -> None:
        if self.allIndicatorsListWidget.hasFocus():
            self.recommendsListWidget.clearSelection()
            self.lastSearchedListWidget.clearSelection()
        elif self.recommendsListWidget.hasFocus():
            self.lastSearchedListWidget.clearSelection()
            self.allIndicatorsListWidget.clearSelection()
        elif self.lastSearchedListWidget.hasFocus():
            self.allIndicatorsListWidget.clearSelection()
            self.recommendsListWidget.clearSelection()

    def find_similar_indicator(self) -> None:
        text = self.searchIndicatorsTextEdit.toPlainText()
        if len(text) > 0:
            self.search_ind_list = [indicator for indicator in self.indicator_list if text.lower() in indicator.lower()]
            self.allIndicatorsListWidget.clear()
            self.allIndicatorsListWidget.addItems(self.search_ind_list)
            self.full_list_active = False
        else:
            self.allIndicatorsListWidget.clear()
            self.allIndicatorsListWidget.addItems(self.indicator_list)
            self.full_list_active = True

    def accept_indicator(self) -> None:
        row_number_all = self.allIndicatorsListWidget.currentRow()
        row_number_rec = self.recommendsListWidget.currentRow()
        row_number_last = self.lastSearchedListWidget.currentRow()

        if row_number_all != -1:
            if self.full_list_active:
                self.accepted_indicator = self.indicator_list[row_number_all]
            else:
                self.accepted_indicator = self.search_ind_list[row_number_all]
        elif row_number_rec != -1:
            self.accepted_indicator = self.recommended_indicators[row_number_rec]
        elif row_number_last != -1:
            self.accepted_indicator = self.last_used_indicators[::-1][row_number_last]

        self.main_window.change_info_text(
            self.indicator_number,
            self.field_name,
            self.accepted_indicator
        )
        self.update_last_used_indicators()
        self.hide()

    def update_last_used_indicators(self) -> None:
        self.last_used_indicators.append(self.accepted_indicator)
        self.lastSearchedListWidget.clear()
        if len(self.last_used_indicators) == 1:
            self.lastSearchedListWidget.addItem(self.last_used_indicators[0])
        else:
            self.lastSearchedListWidget.addItems(self.last_used_indicators[:5][::-1])

    def set_indicator_number(self) -> None:
        self.indicator_number = 2 if "2" in QApplication.instance().sender().objectName() else 1

    def showCYRWidget(self) -> None:
        self.set_indicator_number()

        self.updateIndicatorsToolButton.clicked.connect(self.update_CYR)

        self.setWindowTitle(f'Выбор показателей ЦУР')
        self.field_name = "ЦУР"

        self.allIndicatorsListWidget.clear()
        self.indicator_list = industries_indicators.indicators["CYR"]
        self.allIndicatorsListWidget.addItems(self.indicator_list)

        self.show()

    def update_CYR(self) -> None:
        DBInteraction.CYR.run()
        self.allIndicatorsListWidget.clear()
        self.indicator_list = industries_indicators.indicators["CYR"]
        self.allIndicatorsListWidget.addItems(self.indicator_list)

    def showStrategyWidget(self) -> None:
        self.set_indicator_number()

        self.updateIndicatorsToolButton.clicked.connect(self.update_Strategy)

        self.setWindowTitle(f'Выбор показателей Стратегии развития')
        self.field_name = "Стратегия развития"

        self.allIndicatorsListWidget.clear()
        self.indicator_list = industries_indicators.indicators["Strategies"]
        self.allIndicatorsListWidget.addItems(self.indicator_list)

        self.show()

    def update_Strategy(self) -> None:
        DBInteraction.strategies.run()
        self.allIndicatorsListWidget.clear()
        self.indicator_list = industries_indicators.indicators["Strategies"]
        self.allIndicatorsListWidget.addItems(self.indicator_list)

    def showPMWidget(self) -> None:
        self.set_indicator_number()

        self.updateIndicatorsToolButton.clicked.connect(self.update_PM)

        self.setWindowTitle(f'Выбор показателей Плана мероприятий')
        self.field_name = "План мероприятий"

        self.allIndicatorsListWidget.clear()
        self.indicator_list = industries_indicators.indicators["PM"]
        self.allIndicatorsListWidget.addItems(self.indicator_list)

        self.show()

    def update_PM(self) -> None:
        DBInteraction.PM.run()
        self.allIndicatorsListWidget.clear()
        self.indicator_list = industries_indicators.indicators["PM"]
        self.allIndicatorsListWidget.addItems(self.indicator_list)