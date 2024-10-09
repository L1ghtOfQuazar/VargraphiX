import sys  # sys нужен для передачи argv в QApplication
import os  # Отсюда нам понадобятся методы для отображения содержимого директорий

from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QTableWidgetItem

from design import *
from csvopener import *

class ExampleApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.pushButton.clicked.connect(self.browse_folder)  # Выполнить функцию browse_folder
                                                            # при нажатии кнопки

    def browse_folder(self):
        self.tableWidget.clear()  # На случай, если в списке уже есть элементы
        directory = QtWidgets.QFileDialog.getOpenFileNames(self, "Выберите файл")
        # открыть диалог выбора директории и установить значение переменной
        # равной пути к выбранной директории

        if directory:  # не продолжать выполнение, если пользователь не выбрал директорию
            d = directory[0][0]
            openfile(d)
            x, y, f, r = data_reading(d)
            self.tableWidget.setColumnCount(x)  # Set three columns
            self.tableWidget.setRowCount(y)
            f = fieldnamenormaliser(f)
            self.tableWidget.setHorizontalHeaderLabels(f)
            for i in range(x):
                for j in range(y):
                    self.tableWidget.setItem(i, j, QTableWidgetItem(r[i][j]))
            self.tableWidget.resizeColumnsToContents()

def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec()  # и запускаем приложение

if __name__ == '__main__':
    main()