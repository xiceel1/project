from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(783, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listApart = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.listApart.setGeometry(QtCore.QRect(10, 90, 691, 351))
        self.listApart.setObjectName("listApart")
        self.searchButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.searchButton.setGeometry(QtCore.QRect(470, 40, 75, 23))
        self.searchButton.setObjectName("searchButton")
        self.countryBox = QtWidgets.QComboBox(parent=self.centralwidget)
        self.countryBox.setGeometry(QtCore.QRect(10, 40, 151, 21))
        self.countryBox.setObjectName("countryBox")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 20, 47, 13))
        self.label.setObjectName("label")
        self.priceEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.priceEdit.setGeometry(QtCore.QRect(180, 40, 151, 21))
        self.priceEdit.setObjectName("priceEdit")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(180, 20, 111, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(350, 20, 47, 13))
        self.label_3.setObjectName("label_3")
        self.roomsBox = QtWidgets.QComboBox(parent=self.centralwidget)
        self.roomsBox.setGeometry(QtCore.QRect(350, 40, 69, 22))
        self.roomsBox.setObjectName("roomsBox")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 783, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        __sortingEnabled = self.listApart.isSortingEnabled()
        self.listApart.setSortingEnabled(False)
        self.listApart.setSortingEnabled(__sortingEnabled)
        self.searchButton.setText(_translate("MainWindow", "поиск"))
        self.label.setText(_translate("MainWindow", "Искать в "))
        self.label_2.setText(_translate("MainWindow", "Цена до, ₽ в месяц"))
        self.label_3.setText(_translate("MainWindow", "Комнат"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
