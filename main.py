import sys
import io

from PyQt6.QtWidgets import (QTableWidget, QTableWidgetItem,
                             QWidget, QPushButton, QLabel, QTextEdit, QLineEdit, QMessageBox, )

from sql import *

from PyQt6 import uic
from PyQt6 import QtWidgets

import design
from owners_update import *
from dataBase import *

# create_data_base()
# owners_update()
# flats()
con = sqlite3.connect('rent.db')


class PriceFormatError(Exception):
    pass


class Renting(QWidget):
    def __init__(self, rent_id):
        super().__init__()
        self.setFixedSize(250, 300)

        self.setWindowTitle('Окно подтверждения аренды')

        self.name = QLineEdit(self)
        self.name.move(110, 10)
        self.name.resize(100, 30)
        self.name_label = QLabel(self)
        self.name_label.setText('Введите ФИО:')
        self.name_label.move(10, 15)

        self.phone = QLineEdit(self)
        self.phone.move(110, 50)
        self.phone.resize(100, 30)
        self.phone_label = QLabel(self)
        self.phone_label.setText('Введите телефон:')
        self.phone_label.move(10, 55)

        self.email = QLineEdit(self)
        self.email.move(110, 90)
        self.email.resize(100, 30)
        self.email_label = QLabel(self)
        self.email_label.setText('Введите почту:')
        self.email_label.move(10, 95)

        self.passport = QLineEdit(self)
        self.passport.move(110, 130)
        self.passport.resize(100, 30)
        self.passport_label = QLabel(self)
        self.passport_label.setText('Введите паспорт:')
        self.passport_label.move(10, 135)

        self.accept = QPushButton(self)
        self.accept.clicked.connect(self.renter_adding)
        self.accept.move(80, 240)
        self.accept.resize(100, 50)
        self.accept.setText('Арендовать')

        self.rent_id = rent_id

    def renter_adding(self):
        print(self.rent_id)
        query_rent = f'''
        UPDATE flats 
        SET state = 1
        WHERE id = {self.rent_id}
        '''
        db = DataBase(query_rent)
        db.db_update()


class Rent(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.searchButton.clicked.connect(self.search)

        self.setWindowTitle('Окно выбора квартиры')

        self.stat = QtWidgets.QLabel(self)
        self.stat.move(70, 450)
        self.stat.resize(220, 15)

        self.setFixedSize(783, 600)

        self.rent_button = QPushButton(self)
        self.rent_button.move(66, 490)
        self.rent_button.resize(200, 60)
        self.rent_button.setText('Арендовать квартиру')
        self.rent_button.clicked.connect(self.renting)

        self.rent_id = 0

        self.table_update()

        self.countryBox.addItem('Не важно')
        self.countries = list(con.cursor().execute('''SELECT DISTINCT country FROM flats''').fetchall())
        for c in self.countries:
            self.countryBox.addItem(c[0])

        self.roomsBox.addItem('Не важно')
        self.rooms = list(con.cursor().execute('''SELECT DISTINCT rooms FROM flats'''))
        for r in self.rooms:
            self.roomsBox.addItem(str(r[0]))

        self.prices = list(con.cursor().execute('''SELECT DISTINCT price FROM flats''').fetchall())

    def search(self):
        try:
            self.update()
        except PriceFormatError:
            self.price_error_window('price')

    def table_update(self):
        self.listApart.clear()
        self.listApart.setHorizontalHeaderLabels(
            ('ID', 'Город', 'Улица', 'Кол-во комнат', 'Цена', 'Статус', 'ФИО хозяина', 'ФИО арендующего'))

    def renting(self):
        selected_items = self.listApart.selectedItems()

        if len(selected_items) == 1:
            item = selected_items[0]
            row = item.row()

            self.rent_id = self.listApart.item(row, 0).text()
            self.renting_window = Renting(self.rent_id)
            self.renting_window.show()
            print(self.rent_id)

        elif len(selected_items) > 1:
            QMessageBox.warning(self, "Ошибка", "Пожалуйста, выберите только один элемент.")
        else:
            QMessageBox.warning(self, "Ошибка", "Пожалуйста, выберите хотя бы один элемент.")

    def update(self):
        price = self.priceEdit.text()
        rooms = self.roomsBox.currentText()
        country = self.countryBox.currentText()

        if price != '' and not price.isnumeric():
            raise PriceFormatError

        if country == 'Не важно':
            country = tuple(i[0] for i in self.countries)
        else:
            country = f'("{country}")'

        if rooms == 'Не важно':
            rooms = tuple(int(i[0]) for i in self.rooms)
        else:
            rooms = f'({rooms})'

        if price:
            price = tuple(int(i[0]) for i in self.prices if int(i[0]) <= int(price))
        else:
            price = tuple(int(i[0]) for i in self.prices)

        query = f'''SELECT id, country, street, rooms, price, state, ownerId, renterId FROM flats 
        WHERE price IN {price} AND
        rooms IN {rooms} AND
        country IN {country}
        '''

        res = con.cursor().execute(query).fetchall()

        if not res:
            self.stat.setText('Ничего не найдено')
        else:
            self.stat.setText(f'По запросу найдено элементов: {len(res)}')

        self.table_update()

        self.listApart.setColumnCount(8)
        self.listApart.setRowCount(len(res))

        for i, row in enumerate(res):
            for j, elem in enumerate(row):
                self.listApart.setItem(
                    i, j, QTableWidgetItem(str(elem)))

    def price_error_window(self, error_name):
        QMessageBox.warning(self, "Ошибка", 'Введите число!')
        self.priceEdit.clear()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Rent()
    window.show()
    app.exec()
