# Form implementation generated from reading ui file '3d.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form3d(object):
    def setupUi(self, Form3d):
        Form3d.setObjectName("Form3d")
        Form3d.resize(240, 340)
        Form3d.setMinimumSize(QtCore.QSize(240, 340))
        Form3d.setMaximumSize(QtCore.QSize(240, 340))
        Form3d.setStyleSheet("QWidget {\n"
"    color: #E0FBFC;\n"
"    background-color: #1b2022;\n"
"    font-size: 10pt;\n"
"    font-weight: 600;\n"
"}")
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=Form3d)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(40, 0, 160, 339))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.X = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.X.setMaximumSize(QtCore.QSize(16777215, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.X.setFont(font)
        self.X.setObjectName("X")
        self.verticalLayout.addWidget(self.X)
        self.asd1 = QtWidgets.QComboBox(parent=self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.asd1.sizePolicy().hasHeightForWidth())
        self.asd1.setSizePolicy(sizePolicy)
        self.asd1.setMaximumSize(QtCore.QSize(158, 16777215))
        self.asd1.setObjectName("asd1")
        self.verticalLayout.addWidget(self.asd1)
        self.Y = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.Y.setMaximumSize(QtCore.QSize(16777215, 17))
        self.Y.setObjectName("Y")
        self.verticalLayout.addWidget(self.Y)
        self.asd2 = QtWidgets.QComboBox(parent=self.verticalLayoutWidget)
        self.asd2.setObjectName("asd2")
        self.verticalLayout.addWidget(self.asd2)
        self.Z = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.Z.setMaximumSize(QtCore.QSize(16777215, 17))
        self.Z.setObjectName("Z")
        self.verticalLayout.addWidget(self.Z)
        self.asd3 = QtWidgets.QComboBox(parent=self.verticalLayoutWidget)
        self.asd3.setObjectName("asd3")
        self.verticalLayout.addWidget(self.asd3)
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
        self.conclusion = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.conclusion.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.conclusion.sizePolicy().hasHeightForWidth())
        self.conclusion.setSizePolicy(sizePolicy)
        self.conclusion.setMaximumSize(QtCore.QSize(158, 16777215))
        self.conclusion.setObjectName("conclusion")
        self.verticalLayout.addWidget(self.conclusion)

        self.retranslateUi(Form3d)
        QtCore.QMetaObject.connectSlotsByName(Form3d)

    def retranslateUi(self, Form3d):
        _translate = QtCore.QCoreApplication.translate
        Form3d.setWindowTitle(_translate("Form3d", "Form"))
        self.X.setText(_translate("Form3d", "Элементы оси X"))
        self.Y.setText(_translate("Form3d", "Элементы оси Y"))
        self.Z.setText(_translate("Form3d", "Элементы оси Z"))
        self.label.setText(_translate("Form3d", "Цвет столбцов"))
        self.comboBoxc.setItemText(0, _translate("Form3d", "Красный"))
        self.comboBoxc.setItemText(1, _translate("Form3d", "Зелёный"))
        self.comboBoxc.setItemText(2, _translate("Form3d", "Синий"))
        self.comboBoxc.setItemText(3, _translate("Form3d", "Аквамариновый"))
        self.comboBoxc.setItemText(4, _translate("Form3d", "Розовый"))
        self.comboBoxc.setItemText(5, _translate("Form3d", "Жёлтый"))
        self.conclusion.setText(_translate("Form3d", "Вывод графика"))