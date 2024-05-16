import datetime as dt
import os
import sqlite3
import sys

from PyQt5.QtWidgets import QApplication, QDialog

from data.ui_python.design_for_recordswind import Ui_Dialog


class RecordWind(Ui_Dialog, QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.ok, self.cancel = self.buttonBox.buttons()
        self.ok.clicked.connect(self.fnc_for_ok)
        self.cancel.clicked.connect(self.for_cancel_btn)
        self.record_time = 10

        self.bd = sqlite3.connect('data/db/records_db.sqlite')

    def fnc_for_ok(self):
        try:
            today = str(dt.datetime.now())
            a = today.split()
            date = '.'.join(a[0].split('-')[::-1])
            cur = self.bd.cursor()
            cur.execute(f'''INSERT INTO records VALUES ('{self.lineEdit.text()}', {self.record_time}, '{str(date)}', {1})''')
            self.bd.commit()

        except Exception as e:
            print(e)

    def for_cancel_btn(self):
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wind = RecordWind()
    wind.show()
    sys.exit(app.exec())
