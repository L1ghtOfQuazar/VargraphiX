from main import *
from graph2 import *
from plot import *
from graph3d import *
from diagram import *
from tabled import *
from csvopener import *
import itertools

class Graph2App(QtWidgets.QWidget, Ui_Form2d):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.pushButton.clicked.connect(self.graph2dgen)
        self.setWindowTitle('VargraphiX-2d')
        self.setWindowIcon(QtGui.QIcon('icon.png'))

    def graph2dgen(self):
        col = {'Красный': "'r'", 'Зелёный': "'g'", 'Синий': "'b'", 'Аквамариновый': "'c'", 'Розовый': "'m'", 'Жёлтый': "'y'"}
        file = open('datalog.txt', 'r')
        b = file.readline()
        file.close()
        x1, y1, f, r = data_reading(b)
        f = fieldnamenormaliser(doublenormaliser(f))
        rtrans = list(map(list, itertools.zip_longest(*r, fillvalue=None)))
        x, y = rtrans[int(f.index(self.combo21.currentText()))], rtrans[int(f.index(self.combo22.currentText()))]
        plot2d(x, y, str(self.combo21.currentText()), str(self.combo22.currentText()), col[self.comboBoxc.currentText()])


class Graph3App(QtWidgets.QWidget, Ui_Form3d):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.conclusion.clicked.connect(self.graph3dgen)  # Для 3D графика
        self.setWindowTitle('VargraphiX-3d')
        self.setWindowIcon(QtGui.QIcon('icon.png'))


    def graph3dgen(self):
        file = open('datalog.txt', 'r')
        b = file.readline()
        file.close()
        col = {'Красный': "'r'", 'Зелёный': "'g'", 'Синий': "'b'", 'Аквамариновый': "'c'", 'Розовый': "'m'",
               'Жёлтый': "'y'"}
        x1, y1, f, r = data_reading(b)
        rtrans = list(map(list, itertools.zip_longest(*r, fillvalue=None)))
        f = fieldnamenormaliser(doublenormaliser(f))
        x, y, z = rtrans[int(f.index(self.asd1.currentText()))], rtrans[int(f.index(self.asd2.currentText()))], rtrans[int(f.index(self.asd3.currentText()))]
        plot3d(x, y, z, str(self.asd1.currentText()), str(self.asd2.currentText()), str(self.asd3.currentText()), col[self.comboBoxc.currentText()])


class Graph4App(QtWidgets.QWidget, Ui_Formp):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.conclusion.clicked.connect(self.pie_chart_gen)  # Для круговой диаграммы
        self.setWindowTitle('VargraphiX-Pie')
        self.setWindowIcon(QtGui.QIcon('icon.png'))


    def pie_chart_gen(self):
        file = open('datalog.txt', 'r')
        b = file.readline()
        file.close()
        x1, y1, f, r = data_reading(b)
        rtrans = list(map(list, itertools.zip_longest(*r, fillvalue=None)))
        f = fieldnamenormaliser(doublenormaliser(f))
        values = rtrans[int(f.index(self.add1.currentText()))]
        labels = rtrans[int(f.index(self.add1.currentText()))]
        values = [str(i) for i in values]
        labels = [str(i) for i in labels]
        k = dict()
        sh = 0
        for j in values:
            k[labels[sh]] = values.count(j) / len(values)
            sh = sh + 1
        values, labels = [], []
        for key, value in k.items():
            labels.append(key)
            values.append(value)
        labels = "{'" + "', '".join(labels) + "'}"
        plot_pie(labels, values, self.add1.currentText())


class Graph5App(QtWidgets.QWidget, Ui_Formt):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.pushButton.clicked.connect(self.bar_chart_gen)  # Для столбчатой диаграммы
        self.setWindowTitle('VargraphiX-Bar')
        self.setWindowIcon(QtGui.QIcon('icon.png'))

    def bar_chart_gen(self):
        file = open('datalog.txt', 'r')
        b = file.readline()
        file.close()
        x1, y1, f, r = data_reading(b)
        col = {'Красный': "'r'", 'Зелёный': "'g'", 'Синий': "'b'", 'Аквамариновый': "'c'", 'Розовый': "'m'", 'Жёлтый': "'y'"}
        f = fieldnamenormaliser(doublenormaliser(f))
        rtrans = list(map(list, itertools.zip_longest(*r, fillvalue=None)))
        labels, values = str(self.combo22.currentText()), rtrans[int(f.index(self.combo22.currentText()))]
        values = [float(i) for i in values]
        plot_bar(labels, values, col[self.comboBoxc.currentText()])