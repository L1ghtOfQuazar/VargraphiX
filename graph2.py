# Form implementation generated from reading ui file 'graph2.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form2d(object):
    def setupUi(self, Form2d):
        Form2d.setObjectName("Form2d")
        Form2d.resize(210, 300)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form2d.sizePolicy().hasHeightForWidth())
        Form2d.setSizePolicy(sizePolicy)
        Form2d.setMinimumSize(QtCore.QSize(210, 300))
        Form2d.setMaximumSize(QtCore.QSize(210, 300))
        Form2d.setStyleSheet("QWidget {\n"
"    color: #E0FBFC;\n"
"    background-color: #1b2022;\n"
"    font-size: 10pt;\n"
"    font-weight: 600;\n"
"}")
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=Form2d)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(40, 20, 136, 261))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.combo22 = QtWidgets.QComboBox(parent=self.verticalLayoutWidget)
        self.combo22.setObjectName("combo22")
        self.verticalLayout.addWidget(self.combo22)
        self.label_2 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.combo21 = QtWidgets.QComboBox(parent=self.verticalLayoutWidget)
        self.combo21.setObjectName("combo21")
        self.verticalLayout.addWidget(self.combo21)
        self.label_3 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 17))
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
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

        self.retranslateUi(Form2d)
        QtCore.QMetaObject.connectSlotsByName(Form2d)

    def retranslateUi(self, Form2d):
        _translate = QtCore.QCoreApplication.translate
        Form2d.setWindowTitle(_translate("Form2d", "Form"))
        self.label.setText(_translate("Form2d", "Элементы оси X"))
        self.label_2.setText(_translate("Form2d", "Элементы оси Y"))
        self.label_3.setText(_translate("Form2d", "Цвет столбцов"))
        self.comboBoxc.setItemText(0, _translate("Form2d", "Красный"))
        self.comboBoxc.setItemText(1, _translate("Form2d", "Зелёный"))
        self.comboBoxc.setItemText(2, _translate("Form2d", "Синий"))
        self.comboBoxc.setItemText(3, _translate("Form2d", "Аквамариновый"))
        self.comboBoxc.setItemText(4, _translate("Form2d", "Розовый"))
        self.comboBoxc.setItemText(5, _translate("Form2d", "Жёлтый"))
        self.pushButton.setText(_translate("Form2d", "Вывод графика"))
