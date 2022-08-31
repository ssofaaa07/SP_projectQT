import os
import sys

from PyQt5.QtWidgets import QApplication

os.system("python -m PyQt5.uic.pyuic -x uiFiles/MainWindow.ui -o uiFiles/MainWindow.py")
os.system("python -m PyQt5.uic.pyuic -x uiFiles/IndSubMenuWidget.ui -o uiFiles/IndSubMenuWidget.py")
os.system("python -m PyQt5.uic.pyuic -x uiFiles/IndSubMenuWidget1.ui -o uiFiles/IndSubMenuWidget1.py")


if __name__ == '__main__':
    from classes.SPMainWindow import SPMainWindow

    app = QApplication(sys.argv)
    ex = SPMainWindow()
    sys.exit(app.exec_())
