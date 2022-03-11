import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from Roxy_Layout import Ui_Roxy
from Main_Roxie import Roxy

class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.uic = Ui_Roxy()
        self.uic.setupUi(self.main_win)
        self.uic.Start_Button.click.connect(lambda: self.Start_Roxy())

    def Start_Roxy(self):
        Roxy()

    def show(self):
        self.main_win.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())
