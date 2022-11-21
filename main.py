import sys
import sqlite3


from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5 import uic


class Coffee(QMainWindow):
    def __init__(self):
        super().__init__()
        self.con = sqlite3.connect('coffee.sqlite')
        uic.loadUi('main.ui', self)

        self.show_coffees()

    def show_coffees(self):
        cur = self.con.cursor()
        data = cur.execute("""SELECT * FROM coffee""").fetchall()
        title = ['ID', 'название сорта', 'степень обжарки',
                 'молотый/в зернах', 'описание вкуса', 'цена', 'объем упаковки']

        self.tableWidget.setColumnCount(len(title))
        self.tableWidget.setHorizontalHeaderLabels(title)
        self.tableWidget.setRowCount(0)
        for i, row in enumerate(data):
            self.tableWidget.setRowCount(
                self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(
                    i, j, QTableWidgetItem(elem))
        self.tableWidget.resizeColumnsToContents()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    prog = Coffee()
    prog.show()
    sys.exit(app.exec())