import sys

from PyQt5.QtCore import QTimer, QSize
from PyQt5.QtGui import QIcon, QFont, QPalette, QBrush, QPixmap, QKeySequence
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QShortcut, QLabel

from data.windows.record_window import RecordWind
from data.ui_python.sweeper_design import Ui_Form
from data.logic.sweeper_logic import Sweeper


class SweeperWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setWindowTitle('Сапер')
        self.setFixedSize(417, 570)

        self.bomb_img = QPixmap('data/images/bomb_img.png')
        self.bomb_label = QLabel(self)
        self.bomb_label.resize(200, 200)
        self.bomb_label.move(120, 180)
        self.bomb_label.setPixmap(self.bomb_img)

        # make field buttons
        self.buttons = {}

        for y in range(70, 490, 42):
            for x in range(0, 420, 42):
                btn = QPushButton(self)
                btn.resize(43, 43)
                btn.move(x, y)
                btn.setFont(QFont('Roboto', 15))
                btn.clicked.connect(self.fnc_for_field_buttons)
                self.buttons[btn] = (x // 42, (y - 70) // 42)

        # start timer
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.change_time)
        self.timer.setInterval(1000)
        self.timer.start()
        self.time = -1
        self.time_lcd.setStyleSheet('color: white')

        # smile btn settings
        self.icon = QIcon('data/images/smile.png')
        self.smile_button.setText('')
        self.smile_button.setIcon(self.icon)
        self.smile_button.setIconSize(QSize(68, 70))
        self.smile_button.clicked.connect(self.fnc_for_smile)

        # set dig is True and set fonts
        self.is_dig.setChecked(True)
        self.is_dig.setFont(QFont('Roboto', 13))
        self.is_dig.resize(100, 30)

        # set font for flag btn
        self.is_flag.setFont(QFont('Roboto', 13))
        self.is_flag.resize(200, 30)

        # make sweeper class
        self.sweep = Sweeper()

        # show bombs quantity
        self.bombs_lcd.display(self.sweep.flags_col)
        self.bombs_lcd.setStyleSheet('color: white')

        # button for developer
        self.cheat_btn = QPushButton('cheat', self)
        self.cheat_btn.clicked.connect(self.cheat)
        self.cheat_btn.close()

        # dict with button colors
        self.colors = {'0': (0, 0, 0), '1': '#00008B', '2': '#32CD32', '3': '#B22222', '4': '#4B0082', '5': '#8B4513',
                       '6': '#2E4922', '7': '#4DCFD5', '8': '#FFC805', '9': 'Такого не бывает'}

        # set background image
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(QPixmap("data/images/background.png")))
        self.setPalette(palette)

        self.record_window = RecordWind()

        self.shortcut = QShortcut(QKeySequence("Shift+c"), self)
        self.shortcut.activated.connect(self.change_dig_flag)

    def change_time(self):
        # function for time
        self.time += 1
        self.time_lcd.display(self.time)

    def fnc_for_field_buttons(self):
        # function for field buttons
        try:
            # getting coordinates of clicked button
            x, y = self.buttons[self.sender()]

            # making field in sweeper class
            if not self.sweep.moves and self.is_dig.isChecked():
                self.sweep.make_field(x, y)
                self.fill_field()
                self.bombs_lcd.display(self.sweep.flags_col)

            # dig button
            elif self.is_dig.isChecked() and not self.sender().text():
                self.sweep.dig(x, y)

            # put or remove flag from field
            elif self.is_flag.isChecked() and (
                    not self.sweep.player_field[x][y] or self.sweep.player_field[x][y] == 'F'):
                # remove
                if self.sweep.player_field[x][y] == 'F':
                    self.sweep.remove_flag(x, y)
                # put
                else:
                    self.sweep.put_flag(x, y)
                # change bombs quantity
                self.bombs_lcd.display(self.sweep.flags_col)

            # checking clicked button
            elif self.sender().text():
                check_result = self.sweep.check(x, y)

                # if all is right and we can make check
                if check_result is True:
                    self.sweep.make_check(x, y)

                # if something wrong but you didn't lose yet
                elif check_result is None:
                    pass

                # if something wrong and you lose
                else:
                    self.fill_field()
                    # send message to ask about new game
                    valid = QMessageBox.question(self, 'Вы проиграли', 'Хотите начать заново?', QMessageBox.Yes,
                                                 QMessageBox.No)
                    if valid == QMessageBox.Yes:
                        self.fnc_for_smile()
                    else:
                        self.close()

            # check win or lose
            if self.sweep.moves:
                win_or_lose = self.sweep.win_or_lose()
                # if win send a message for a new game
                if win_or_lose:
                    self.fill_field()
                    self.record_window.show()
                    self.record_window.record_time = self.time
                    valid = QMessageBox.question(self, 'Вы победили', 'Хотите начать заново?', QMessageBox.Yes,
                                                 QMessageBox.No)
                    if valid == QMessageBox.Yes:
                        self.fnc_for_smile()
                    else:
                        self.close()
                    self.timer.stop()

                # if lose send a message for a new game
                elif win_or_lose is False:
                    self.fill_field()
                    valid = QMessageBox.question(self, 'Вы проиграли', 'Хотите начать заново?', QMessageBox.Yes,
                                                 QMessageBox.No)
                    if valid == QMessageBox.Yes:
                        self.fnc_for_smile()
                    else:
                        self.close()

                self.fill_field()

        except Exception as e:
            print(e)

    def fill_field(self):
        # fnc to fill field
        for btn, c in self.buttons.items():
            if self.sweep.player_field[c[0]][c[1]] == '0':
                around = self.sweep.poles_around(c[0], c[1])
                for i in around:
                    if not self.sweep.player_field[i[0]][i[1]]:
                        break
                else:
                    btn.close()

            if self.sweep.player_field[c[0]][c[1]] == 'F':
                btn.setText('🚩')
                continue

            if self.sweep.player_field[c[0]][c[1]] == 'B':
                btn.setText('💣')
                continue
            if self.sweep.player_field[c[0]][c[1]]:
                btn.setStyleSheet(f'color: {self.colors[self.sweep.player_field[c[0]][c[1]]]}')

            btn.setText(self.sweep.player_field[c[0]][c[1]])

    def fnc_for_smile(self):
        # if smile btn clicked clear field
        for btn in self.buttons:
            btn.setIcon(QIcon())
            btn.show()
            btn.setText('')
        self.time = 0
        self.sweep = Sweeper()
        self.bombs_lcd.display(self.sweep.flags_col)
        self.is_dig.setChecked(True)

    def cheat(self):
        # for developer
        self.sweep.pretty_field_print(self.sweep.field)
        print(set(self.sweep.bombs_coordinates) & set(self.sweep.flags_coordinates))
        print(self.sweep.flags_coordinates)
        print(self.sweep.bombs_coordinates)

    def change_dig_flag(self):
        if self.is_dig.isChecked():
            self.is_flag.setChecked(True)
        else:
            self.is_dig.setChecked(True)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wind = SweeperWindow()
    wind.show()
    sys.exit(app.exec())
