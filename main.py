import sys
import sqlite3

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox
from PyQt5 import uic


class Coffee(QMainWindow):
    def __init__(self):
        super().__init__()
        self.con = sqlite3.connect('coffee.sqlite')
        uic.loadUi('main.ui', self)

        self.pushButton.clicked.connect(self.add_coffee)
        self.pushButton_2.clicked.connect(self.edit_coffee)

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
                    i, j, QTableWidgetItem(str(elem)))
        self.tableWidget.resizeColumnsToContents()

    def add_coffee(self):
        prog_2.show()
        prog_2.load_boxes()
        prog_2.setWindowTitle('Добавить кофе')
        prog_2.pushButton.setText('Добавить')
        prog_2.pushButton.clicked.connect(prog_2.add)
        prog_2.clear_all()

    def edit_coffee(self):
        prog_2.load_boxes()
        if prog_2.insert():
            prog_2.show()
            prog_2.setWindowTitle('Редактировать кофе')
            prog_2.pushButton.setText('Редактировать')
            prog_2.pushButton.clicked.connect(prog_2.edit)


class AddEdit(QMainWindow):
    def __init__(self):
        super().__init__()
        self.con = sqlite3.connect('coffee.sqlite')
        self.cur = self.con.cursor()
        self.temp = list()
        self.temp_2 = list()
        self.id = 0
        uic.loadUi('addEditCoffeeForm.ui', self)

        self.spinBox.setMaximum(10000)
        self.spinBox_2.setMaximum(10000)

    def add(self):
        valid = QMessageBox.question(
            self, ' ', 'Действительно добавить?',
            QMessageBox.Yes, QMessageBox.No)

        if valid == QMessageBox.Yes:
            name = self.lineEdit.text()
            degree_of_roast = self.comboBox.currentText()
            ground_or_in_grains = self.comboBox_2.currentText()
            taste = self.lineEdit_2.text()
            price = self.spinBox.value()
            volume = self.spinBox_2.value()

            if not (name and taste):
                QMessageBox.warning(self, ' ', 'Введены не все данные', QMessageBox.Ok)
            else:
                self.cur.execute("""INSERT INTO coffee(variety, degree_of_roast,
                                    ground_or_in_grains, taste_description, 
                                    price, packing_volume) VALUES (?, ?, ?, ?, ?, ?)""",
                                 (name, degree_of_roast, ground_or_in_grains, taste, price, volume))
                self.con.commit()

            prog.show_coffees()
            prog_2.hide()

    def edit(self):
        valid = QMessageBox.question(
            self, ' ', 'Действительно изменить?',
            QMessageBox.Yes, QMessageBox.No)

        if valid == QMessageBox.Yes:
            name = self.lineEdit.text()
            degree_of_roast = self.comboBox.currentText()
            ground_or_in_grains = self.comboBox_2.currentText()
            taste = self.lineEdit_2.text()
            price = self.spinBox.value()
            volume = self.spinBox_2.value()

            if not (name and taste):
                QMessageBox.warning(self, ' ', 'Введены не все данные', QMessageBox.Ok)
            else:
                self.cur.execute("""UPDATE coffee
                                    SET variety = ?, degree_of_roast = ?,
                                        ground_or_in_grains = ?, taste_description = ?, 
                                        price = ?, packing_volume = ?
                                    WHERE ID = ?""",
                                 (name, degree_of_roast, ground_or_in_grains, taste, price, volume, self.id))
                self.con.commit()

            prog.show_coffees()
            prog_2.hide()

    def insert(self):
        rows = list(set([i.row() for i in prog.tableWidget.selectedItems()]))

        if len(rows) != 1:
            prog.statusBar().showMessage('Выберите одно кофе', 1200)
            return
        else:
            id_of_coffee = prog.tableWidget.item(rows[0], 0).text()
            self.id = id_of_coffee
            data = self.cur.execute("""SELECT * FROM coffee WHERE ID = ?""", (id_of_coffee, )).fetchone()

            self.lineEdit.setText(data[1])
            self.comboBox.setCurrentIndex(self.temp.index(data[2]))
            self.comboBox_2.setCurrentIndex(self.temp_2.index(data[3]))
            self.lineEdit_2.setText(data[4])
            self.spinBox.setValue(data[5])
            self.spinBox_2.setValue(data[6])
            return True

    def clear_all(self):
        self.lineEdit.setText('')
        self.comboBox.setCurrentIndex(0)
        self.comboBox_2.setCurrentIndex(0)
        self.lineEdit_2.setText('')
        self.spinBox.setValue(0)
        self.spinBox_2.setValue(0)

    def load_boxes(self):
        data = self.cur.execute(
            """SELECT degree_of_roast, ground_or_in_grains FROM coffee""").fetchall()

        self.comboBox.clear()
        self.comboBox_2.clear()
        self.temp.clear()
        self.temp_2.clear()

        for i in data:
            self.comboBox.addItem(i[0])
            self.temp.append(i[0])
            self.comboBox_2.addItem(i[1])
            self.temp_2.append(i[1])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    prog = Coffee()
    prog_2 = AddEdit()
    prog.show()
    prog_2.hide()
    sys.exit(app.exec())
