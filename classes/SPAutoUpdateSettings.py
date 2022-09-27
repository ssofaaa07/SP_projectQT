from PyQt5.QtWidgets import QMainWindow, QDialog

from classes.DBThreadInteraction import DBInteraction
from uiFiles.UpdateSettings import Ui_Dialog


class SPAutoUpdateSettings(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        # uic.loadUi('uiFiles/MainWindow.ui', self) # Подгрузка из ui файла
        self.setupUi(self)  # Подгрузка из py класса
        self.setWindowTitle('Настройка')
        self.buttonBox.accepted.connect(self.update_settings)

    def update_settings(self):
        mins = self.minSpinBox.text()
        secs = self.secSpinBox.text()
        if not ((mins == 0 and secs == 0) or (mins == 0 and secs <= 5)):
            DBInteraction.time_to_wait = int(mins) * 60 + int(secs)

        self.hide()
