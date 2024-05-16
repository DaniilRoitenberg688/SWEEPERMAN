import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QTableWidget, QAbstractItemView
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem


class DBSample(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(417, 570)
        self.connection = sqlite3.connect("data/db/records_db.sqlite")
        self.resize(420, 570)
        self.tableWidget = QTableWidget(self)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.setStyleSheet("QMainWindow{ background-image: url(background.png); }")
        self.select_data()
        self.setWindowTitle('Рекорды')


    def select_data(self):
        query = "SELECT name, time, date, levels.level FROM records LEFT JOIN levels ON levels.id = records.level"
        res = self.connection.cursor().execute(query).fetchall()
        self.tableWidget.resize(420, len(res) * 51)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(len(res))
        self.tableWidget.setColumnWidth(0, 99)
        self.tableWidget.setColumnWidth(1, 99)
        self.tableWidget.setColumnWidth(2, 99)
        self.tableWidget.setColumnWidth(3, 99)
        self.tableWidget.setHorizontalHeaderLabels(['Имя', 'Время', 'Дата', 'Сложность'])
        for i in range(len(res)):
            for j in range(4):
                self.tableWidget.setItem(
                    i, j, QTableWidgetItem(str(res[i][j])))

    def closeEvent(self, event):
        self.connection.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DBSample()
    ex.show()
    sys.exit(app.exec())