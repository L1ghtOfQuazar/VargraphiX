from main import *
from graph2 import *
from plot import *
from csvopener import *
import itertools

class Graph2App(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.pushButton.clicked.connect(self.graph2dgen)
        self.pushButton_3d.clicked.connect(self.graph3dgen)  # Для 3D графика
        self.pushButton_bar.clicked.connect(self.bar_chart_gen)  # Для столбчатой диаграммы
        self.pushButton_pie.clicked.connect(self.pie_chart_gen)  # Для круговой диаграммы
        self.setWindowTitle('VargraphiX-2d')
        self.setWindowIcon(QtGui.QIcon('icon.png'))

    def graph2dgen(self):
        file = open('datalog.txt', 'r')
        b = file.readline()
        file.close()
        x1, y1, f, r = data_reading(b)
        f = fieldnamenormaliser(doublenormaliser(f))
        rtrans = list(map(list, itertools.zip_longest(*r, fillvalue=None)))
        x, y = rtrans[int(f.index(self.combo21.currentText()))], rtrans[int(f.index(self.combo22.currentText()))]
        plot2d(x, y)

    def graph3dgen(self):
        file = open('datalog.txt', 'r')
        b = file.readline()
        file.close()
        x1, y1, f, r = data_reading(b)
        rtrans = list(map(list, itertools.zip_longest(*r, fillvalue=None)))
        x, y, z = rtrans[int(self.combo31.currentText())], rtrans[int(self.combo32.currentText())], rtrans[int(self.combo33.currentText())]
        plot3d(x, y, z)

    def bar_chart_gen(self):
        file = open('datalog.txt', 'r')
        b = file.readline()
        file.close()
        x1, y1, f, r = data_reading(b)
        rtrans = list(map(list, itertools.zip_longest(*r, fillvalue=None)))
        labels, values = rtrans[int(self.combo41.currentText())], rtrans[int(self.combo42.currentText())]
        plot_bar(labels, values)

    def pie_chart_gen(self):
        file = open('datalog.txt', 'r')
        b = file.readline()
        file.close()
        x1, y1, f, r = data_reading(b)
        rtrans = list(map(list, itertools.zip_longest(*r, fillvalue=None)))
        labels, values = rtrans[int(self.combo51.currentText())], rtrans[int(self.combo52.currentText())]
        plot_pie(labels, values)
