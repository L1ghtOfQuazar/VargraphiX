from main import *
from graph2 import *
from plot import *
from csvopener import *

class Graph2App(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.pushButton.clicked.connect(self.graph2dgen)
        self.setWindowTitle('VargraphiX-2d')
        self.setWindowIcon(QtGui.QIcon('icon.png'))

    def graph2dgen(self):

        file = open('datalog.txt', 'r')
        b = file.readline()
        file.close()
        x1, y1, f, r = data_reading(b)
        rtrans = list(map(list, itertools.zip_longest(*r, fillvalue=None)))
        x, y = rtrans[int(self.combo21.currentText())], rtrans[int(self.combo22.currentText())]
        plot2d(x, y)