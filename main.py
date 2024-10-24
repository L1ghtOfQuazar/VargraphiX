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
        self.graph2.setEnabled(False)
        self.graph3.setEnabled(False)
        self.pie.setEnabled(False)
        self.Filtrs_7.setEnabled(False)
        self.upd.setEnabled(False)
        self.open.clicked.connect(self.browse_folder)
        self.upd.clicked.connect(self.update)
        self.graph2.clicked.connect(self.show_graph2)
        self.graph3.clicked.connect(self.show_graph3)
        self.pie.clicked.connect(self.show_graph4)
        self.filter.clicked.connect(self.oct)
        self.Filtrs_7.clicked.connect(self.show_graph5)# Выполнить функцию browse_folder
        self.setWindowTitle('VargraphiX')
        self.setWindowIcon(QtGui.QIcon('icon.png'))

    def oct(self):
        os.popen("octave --gui")

    def update(self):
        file = open('datalog.txt', 'r')
        d = file.readline()
        file.close()
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
                self.graph2.setEnabled(True)
                self.graph3.setEnabled(True)
                self.pie.setEnabled(True)
                self.Filtrs_7.setEnabled(True)
                self.upd.setEnabled(True)
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

    def show_graph3(self):
        self.windowgraph3d = Graph3App()  # Создаём объект класса ExampleApp
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
                self.windowgraph3d.asd1.addItem(cn[0])
                self.windowgraph3d.asd2.addItem(cn[0])
                self.windowgraph3d.asd3.addItem(cn[0])
        self.windowgraph3d.show()  # Показываем окно

    def show_graph4(self):
        self.windowgraphpie = Graph4App()  # Создаём объект класса ExampleApp
        datalog = open("datalog.txt", "r")
        d = datalog.readline()
        datalog.close()
        x, y, f, r = data_reading(d)
        f = fieldnamenormaliser(doublenormaliser(f))
        file = open('openlog.txt', 'r')
        b = file.readline()
        file.close()
        c = []
        for i in f:
            self.windowgraphpie.add1.addItem(i)
        self.windowgraphpie.show()  # Показываем окно

    def show_graph5(self):
        self.windowgraphs = Graph5App()  # Создаём объект класса ExampleApp
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
                self.windowgraphs.combo22.addItem(cn[0])
        self.windowgraphs.show()  # Показываем окно

def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = MainApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec()  # и запускаем приложение

if __name__ == '__main__':
    main()