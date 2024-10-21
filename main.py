import sys
import os
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QTableWidgetItem, QMessageBox
from PyQt6 import QtCore
from PyQt6 import QtGui
from graph2d import *
from design import *
from csvopener import *
from plot import *
import time
import itertools
class MainApp(QtWidgets.QMainWindow, Ui_VargraphiX):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.open.clicked.connect(self.browse_folder)
        self.graph2.clicked.connect(self.show_graph2)# Выполнить функцию browse_folder
        self.setWindowTitle('VargraphiX')
        self.setWindowIcon(QtGui.QIcon('icon.png'))

    def browse_folder(self):
        # self.tableWidget.clear()  # На случай, если в списке уже есть элементы
        # self.tableWidget.setColumnCount(0)
        # self.tableWidget.setRowCount(0)
        directory = QtWidgets.QFileDialog.getOpenFileNames(self, "Выберите файл", None, "*.csv")
        # открыть диалог выбора директории и установить значение переменной
        # равной пути к выбранной директории
        if directory[0] != []:  # не продолжать выполнение, если пользователь не выбрал директорию
            d = directory[0][0]
            datalog = open("datalog.txt", "w+")
            datalog.write(f'{d}')
            datalog.close()
            x, y, f, r = data_reading(d)
            self.tableWidget.setColumnCount(x)
            self.tableWidget.setRowCount(y)
            self.tableWidget.setHorizontalHeaderLabels(fieldnamenormaliser(doublenormaliser(f)))
            try:
                for i in range(y):
                    for j in range(x):
                        self.tableWidget.setItem(i, j, QTableWidgetItem(r[i][j]))
                self.tableWidget.resizeColumnsToContents()
                rtrans = list(map(list, itertools.zip_longest(*r, fillvalue=None)))
                intcol = []
                sh = 0
                for i in rtrans:
                    a = True
                    for j in i:
                        try:
                            k = eval(j)
                        except:
                            a = False
                            break
                    if a:
                        intcol.append(sh)
                    sh = sh + 1
                openlog = open("openlog.txt", "w+")
                openlog.write(f'{intcol}')
                openlog.close()
            except:
                self.tableWidget.clear()
                QMessageBox.critical(self, "Ошибка ", "Файл повреждён или составлен неправильно!")


    def show_graph2(self):
        self.windowgraph2d = Graph2App()  # Создаём объект класса ExampleApp
        datalog = open("datalog.txt", "r")
        d = datalog.readline()
        datalog.close()
        x, y, f, r = data_reading(d)
        f = fieldnamenormaliser(doublenormaliser(f))
        file = open('openlog.txt', 'r')
        b = file.readline()
        file.close()
        c = []
        for i in b:
            if i not in [' ', ',', '[', ']']:
                l = []
                l.append(f[int(i)])
                cn = l
                self.windowgraph2d.combo21.addItem(cn[0])
                self.windowgraph2d.combo22.addItem(cn[0])
        self.windowgraph2d.show()  # Показываем окно

def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = MainApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec()  # и запускаем приложение

if __name__ == '__main__':
    main()