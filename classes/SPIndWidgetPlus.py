from PyQt5.QtWidgets import QDialog, QApplication

from classes.DBThreadInteraction import DBInteraction
from classes.IndustriesIndicators import industries_indicators
from uiFiles.IndSubMenuWidget1 import Ui_Form as IndWidgetPlus
from classes.RequestDB import RequestDB, RequestDBPlus


class SPIndWidgetPlus(QDialog, IndWidgetPlus):
    def __init__(self):
        super().__init__()
        # uic.loadUi('uiFiles/IndSubMenuWidget.ui', self) # Подгрузка из ui файла
        self.setupUi(self)  # Подгрузка из py класса
        self.main_window = None

        self.indicator_list = []
        self.search_ind_list = []
        self.last_used_indicators = []
        self.recommended_indicators = []

        self.accepted_indicator = ''

        self.request_DBPlus = None

        self.full_list_active = True
        self.indicator_number = None
        self.type = 0
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
            self.accepted_indicator,
            self.chooseIndustryComboBox.currentText()
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

    def showGPWidget(self) -> None:
        self.set_indicator_number()

        self.updateIndicatorsToolButton.clicked.connect(self.update_GP)

        self.setWindowTitle(f'Выбор показателей Государственных проектов')
        self.field_name = "Государственные проекты"
        self.indicator_list = industries_indicators.GP_industries_ru
        self.chooseIndustryComboBox.addItems(self.indicator_list)

        self.show()
        self.chooseIndustryComboBox.currentTextChanged.connect(self.load_GP_industry_indicators)

    def showRPWidget(self) -> None:
        self.set_indicator_number()

        self.updateIndicatorsToolButton.clicked.connect(self.request_DBPlus.start)

        self.setWindowTitle(f'Выбор показателей Региональных проектов')
        self.field_name = "Региональные проекты"
        self.indicator_list = industries_indicators.RP_industries_ru
        self.chooseIndustryComboBox.addItems(self.indicator_list)

        self.show()
        self.chooseIndustryComboBox.currentTextChanged.connect(self.load_RP_industry_indicators)

    def load_GP_industry_indicators(self) -> None:
        self.allIndicatorsListWidget.clear()
        self.allIndicatorsListWidget.addItems(
            industries_indicators.indicators_by_industries[
                industries_indicators.GP_industries[self.chooseIndustryComboBox.currentIndex()]
            ]
        )

    def load_RP_industry_indicators(self) -> None:
        self.allIndicatorsListWidget.clear()
        self.allIndicatorsListWidget.addItems(
            industries_indicators.indicators_by_industries[
                industries_indicators.RP_industries[self.chooseIndustryComboBox.currentIndex()]
            ]
        )

    def update_GP(self) -> None:
        DBInteraction.GP.run()
        self.allIndicatorsListWidget.clear()
        self.allIndicatorsListWidget.addItems(industries_indicators.indicators["GP"])

    def update_RP(self) -> None:
        DBInteraction.RP.run()
        self.allIndicatorsListWidget.clear()
        self.allIndicatorsListWidget.addItems(industries_indicators.indicators["RP"])
