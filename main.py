import sys
import sqlite3

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox
from PyQt5 import QtCore, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(690, 555)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 40, 671, 481))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 0, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(110, 0, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 690, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Кофе"))
        self.pushButton.setText(_translate("MainWindow", "Добавить"))
        self.pushButton_2.setText(_translate("MainWindow", "Изменить"))


class Ui_MainWindow_2(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(362, 386)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 10, 341, 204))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setVerticalSpacing(14)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.lineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.comboBox = QtWidgets.QComboBox(self.formLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.comboBox)
        self.comboBox_2 = QtWidgets.QComboBox(self.formLayoutWidget)
        self.comboBox_2.setObjectName("comboBox_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.comboBox_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        self.spinBox_2 = QtWidgets.QSpinBox(self.formLayoutWidget)
        self.spinBox_2.setObjectName("spinBox_2")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.spinBox_2)
        self.spinBox = QtWidgets.QSpinBox(self.formLayoutWidget)
        self.spinBox.setObjectName("spinBox")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.spinBox)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(242, 300, 111, 28))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 362, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Название сорта"))
        self.label_2.setText(_translate("MainWindow", "Степень обжарки"))
        self.label_3.setText(_translate("MainWindow", "Молотый/в зернах"))
        self.label_4.setText(_translate("MainWindow", "Описание вкуса"))
        self.label_5.setText(_translate("MainWindow", "Цена(в рублях)"))
        self.label_6.setText(_translate("MainWindow", "Объем упаковки(в граммах)"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))


class Coffee(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.con = sqlite3.connect('data/coffee.sqlite')
        self.setupUi(self)

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


class AddEdit(QMainWindow, Ui_MainWindow_2):
    def __init__(self):
        super().__init__()
        self.con = sqlite3.connect('data/coffee.sqlite')
        self.cur = self.con.cursor()
        self.temp = list()
        self.temp_2 = list()
        self.id = 0
        self.setupUi(self)

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
