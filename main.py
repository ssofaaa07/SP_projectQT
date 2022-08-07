import sys

from PyQt5.QtWidgets import QApplication, QStyleFactory

from SPMainWindow import SPMainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SPMainWindow()
    sys.exit(app.exec_())
