import sys

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel

from data.windows.show_records_window import DBSample
from data.windows.sweeper_game import SweeperWindow
from data.windows.rules_window import RulesWindow


class Menu(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(750, 225, 417, 570)

        self.setFixedSize(417, 570)

        self.setWindowTitle('Сапер')

        self.sweeperLabel = QLabel('Сапер💣', self)
        self.sweeperLabel.resize(300, 75)
        self.sweeperLabel.move(90, 30)
        self.sweeperLabel.setFont(QFont('Roboto', 40))
        self.sweeperLabel.setStyleSheet('color: white')

        self.play_btn = QPushButton('Играть', self)
        self.play_btn.setGeometry(135, 100 + 50, 150, 60)
        self.play_btn.setFont(QFont('Roboto', 17))
        self.sweeper = SweeperWindow()

        self.records_btn = QPushButton('Рекорды', self)
        self.records_btn.setGeometry(135, 200 + 50, 150, 60)
        self.records_btn.setFont(QFont('Roboto', 17))
        self.records_btn.setStyleSheet('color: rgb(62,95,138)')
        self.records = DBSample()
        self.records_btn.clicked.connect(self.fnc_for_records)

        self.play_btn.clicked.connect(self.fnc_for_play)
        self.play_btn.setStyleSheet('color: rgb(66,133,180)')

        self.rules_btn = QPushButton('Правила', self)
        self.rules_btn.setGeometry(135, 300 + 50, 150, 60)
        self.rules_btn.setFont(QFont('Roboto', 17))
        self.rules_btn.setStyleSheet('color: rgb(100,149,237)')
        self.rules_wnd = RulesWindow()
        self.rules_btn.clicked.connect(self.rules_wnd.show)

        self.exit_btn = QPushButton('Выйти', self)
        self.exit_btn.setGeometry(135, 400 + 50, 150, 60)
        self.exit_btn.setFont(QFont('Roboto', 17))
        self.exit_btn.setStyleSheet('color: rgb(154, 206, 235)')
        self.exit_btn.clicked.connect(self.close)

        self.setStyleSheet("QMainWindow{ background-image: url(data/images/background.png); }")

    def fnc_for_play(self):
        self.sweeper = SweeperWindow()
        self.sweeper.show()

    def fnc_for_records(self):
        self.records = DBSample()
        self.records.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wind = Menu()
    wind.show()
    sys.exit(app.exec())
