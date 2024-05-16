import sys

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QScrollArea


class ScrollLabel(QScrollArea):

    # constructor
    def __init__(self, *args, **kwargs):
        QScrollArea.__init__(self, *args, **kwargs)

        self.setWidgetResizable(True)

        content = QWidget(self)
        self.setWidget(content)

        lay = QVBoxLayout(content)

        self.label = QLabel(content)

        self.label.setWordWrap(True)

        self.label.setStyleSheet("QLabel{ background-image: url(data/images/background.png); }")
        self.label.setFont(QFont('Roboto', 11))

        lay.addWidget(self.label)

    def setText(self, text):

        self.label.setText(text)

    def text(self):
        # getting text of the label
        get_text = self.label.text()

        # return the text
        return get_text


class RulesWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Правила')

        self.setFixedSize(417, 570)

        self.setGeometry(750, 225, 417, 570)
        self.setStyleSheet("QMainWindow{ background-image: url(data/images/background.png); }")

        self.rules_label = ScrollLabel(self)
        self.rules_label.setFont(QFont('Roboto', 11))
        self.rules_label.setGeometry(0, 0, 417, 570)
        self.rules_label.setStyleSheet('color: rgb(255, 255, 255)')
        with open('data/text/rules.txt', 'r', encoding='utf8') as file:
            rules = file.readlines()
            self.rules_label.setText(''.join(rules))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = RulesWindow()
    win.show()
    sys.exit(app.exec())
