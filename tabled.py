# Form implementation generated from reading ui file 'table.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Formt(object):
    def setupUi(self, Formt):
        Formt.setObjectName("Formt")
        Formt.resize(240, 182)
        Formt.setMinimumSize(QtCore.QSize(240, 182))
        Formt.setMaximumSize(QtCore.QSize(240, 182))
        Formt.setStyleSheet("QWidget {\n"
"    color: #E0FBFC;\n"
"    background-color: #1b2022;\n"
"    font-size: 10pt;\n"
"    font-weight: 600;\n"
"}")
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=Formt)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(40, 0, 160, 183))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.label_2.setMaximumSize(QtCore.QSize(105, 17))
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.combo22 = QtWidgets.QComboBox(parent=self.verticalLayoutWidget)
        self.combo22.setObjectName("combo22")
        self.verticalLayout.addWidget(self.combo22)
        self.label = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.label.setMaximumSize(QtCore.QSize(16777215, 17))
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.comboBoxc = QtWidgets.QComboBox(parent=self.verticalLayoutWidget)
        self.comboBoxc.setObjectName("comboBoxc")
        self.comboBoxc.addItem("")
        self.comboBoxc.addItem("")
        self.comboBoxc.addItem("")
        self.comboBoxc.addItem("")
        self.comboBoxc.addItem("")
        self.comboBoxc.addItem("")
        self.verticalLayout.addWidget(self.comboBoxc)
        self.pushButton = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)

        self.retranslateUi(Formt)
        QtCore.QMetaObject.connectSlotsByName(Formt)

    def retranslateUi(self, Formt):
        _translate = QtCore.QCoreApplication.translate
        Formt.setWindowTitle(_translate("Formt", "Form"))
        self.label_2.setText(_translate("Formt", "Элементы оси Y"))
        self.label.setText(_translate("Formt", "Цвет столбцов"))
        self.comboBoxc.setItemText(0, _translate("Formt", "Красный"))
        self.comboBoxc.setItemText(1, _translate("Formt", "Зелёный"))
        self.comboBoxc.setItemText(2, _translate("Formt", "Синий"))
        self.comboBoxc.setItemText(3, _translate("Formt", "Аквамариновый"))
        self.comboBoxc.setItemText(4, _translate("Formt", "Розовый"))
        self.comboBoxc.setItemText(5, _translate("Formt", "Жёлтый"))
        self.pushButton.setText(_translate("Formt", "Вывод диаграммы"))