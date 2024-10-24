# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_VargraphiX(object):
    def setupUi(self, VargraphiX):
        VargraphiX.setObjectName("VargraphiX")
        VargraphiX.resize(748, 469)
        VargraphiX.setMinimumSize(QtCore.QSize(748, 0))
        VargraphiX.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        VargraphiX.setStyleSheet("QWidget {\n"
"    color: #E0FBFC;\n"
"    background-color: #1b2022;\n"
"    font-size: 10pt;\n"
"    font-weight: 600;\n"
"}\n"
"QPushButton {\n"
"    border: 2px solid #5C6B73 ;\n"
"    border-radius: 30px;\n"
"    font: 400 10pt \"Malgun Gothic\";\n"
"    background-color: #5C6B73 ;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #C2DFE3;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #E0FBFC;\n"
"}\n"
"QHeaderView\n"
"{\n"
" Background:transparent; \n"
"}\n"
"QHeaderView::section\n"
"{\n"
" background-color: #1b2022;\n"
" Background:transparent; \n"
"}\n"
"QTableCornerButton::section \n"
"{ \n"
" background-color:#1b2022;\n"
"}")
        VargraphiX.setIconSize(QtCore.QSize(24, 24))
        self.centralwidget = QtWidgets.QWidget(parent=VargraphiX)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout_2.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.open = QtWidgets.QPushButton(parent=self.centralwidget)
        self.open.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.open.sizePolicy().hasHeightForWidth())
        self.open.setSizePolicy(sizePolicy)
        self.open.setMaximumSize(QtCore.QSize(16777215, 30))
        self.open.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.open.setFocusPolicy(QtCore.Qt.FocusPolicy.StrongFocus)
        self.open.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.DefaultContextMenu)
        self.open.setAcceptDrops(False)
        self.open.setStyleSheet("")
        self.open.setObjectName("open")
        self.horizontalLayout_2.addWidget(self.open)
        self.upd = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.upd.sizePolicy().hasHeightForWidth())
        self.upd.setSizePolicy(sizePolicy)
        self.upd.setMaximumSize(QtCore.QSize(16777215, 30))
        self.upd.setObjectName("upd")
        self.horizontalLayout_2.addWidget(self.upd)
        spacerItem = QtWidgets.QSpacerItem(450, 30, QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.filter = QtWidgets.QPushButton(parent=self.centralwidget)
        self.filter.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.filter.sizePolicy().hasHeightForWidth())
        self.filter.setSizePolicy(sizePolicy)
        self.filter.setMaximumSize(QtCore.QSize(16777215, 30))
        self.filter.setSizeIncrement(QtCore.QSize(0, 0))
        self.filter.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.filter.setAcceptDrops(False)
        self.filter.setStyleSheet("")
        self.filter.setObjectName("filter")
        self.horizontalLayout_2.addWidget(self.filter)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.tableWidget = QtWidgets.QTableWidget(parent=self.centralwidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(224, 251, 252))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(224, 251, 252))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(224, 251, 252))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.NoBrush)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(224, 251, 252, 128))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(224, 251, 252))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(224, 251, 252))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(224, 251, 252))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.NoBrush)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(224, 251, 252, 128))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(224, 251, 252))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(224, 251, 252))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(224, 251, 252))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.NoBrush)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(224, 251, 252, 128))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.PlaceholderText, brush)
        self.tableWidget.setPalette(palette)
        self.tableWidget.setStyleSheet("color: #E0FBFC;\n"
"background-color: transparent;\n"
"font: 400 10pt \"Malgun Gothic\";\n"
"border: none;\n"
"gridline-color: #C2DFE3;")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout.addWidget(self.tableWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetFixedSize)
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.graph2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.graph2.setMaximumSize(QtCore.QSize(16777215, 30))
        self.graph2.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.graph2.setAcceptDrops(False)
        self.graph2.setStyleSheet("")
        self.graph2.setObjectName("graph2")
        self.horizontalLayout.addWidget(self.graph2)
        self.graph3 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.graph3.setMaximumSize(QtCore.QSize(16777215, 30))
        self.graph3.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.graph3.setAcceptDrops(False)
        self.graph3.setStyleSheet("")
        self.graph3.setObjectName("graph3")
        self.horizontalLayout.addWidget(self.graph3)
        self.pie = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pie.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pie.sizePolicy().hasHeightForWidth())
        self.pie.setSizePolicy(sizePolicy)
        self.pie.setMaximumSize(QtCore.QSize(16777215, 30))
        self.pie.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.pie.setTabletTracking(False)
        self.pie.setFocusPolicy(QtCore.Qt.FocusPolicy.StrongFocus)
        self.pie.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.DefaultContextMenu)
        self.pie.setAcceptDrops(False)
        self.pie.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.pie.setAutoFillBackground(False)
        self.pie.setStyleSheet("")
        self.pie.setAutoDefault(False)
        self.pie.setDefault(False)
        self.pie.setFlat(False)
        self.pie.setObjectName("pie")
        self.horizontalLayout.addWidget(self.pie)
        self.Filtrs_7 = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Filtrs_7.sizePolicy().hasHeightForWidth())
        self.Filtrs_7.setSizePolicy(sizePolicy)
        self.Filtrs_7.setMinimumSize(QtCore.QSize(0, 30))
        self.Filtrs_7.setMaximumSize(QtCore.QSize(16777215, 30))
        self.Filtrs_7.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.Filtrs_7.setAcceptDrops(False)
        self.Filtrs_7.setStyleSheet("")
        self.Filtrs_7.setObjectName("Filtrs_7")
        self.horizontalLayout.addWidget(self.Filtrs_7)
        self.verticalLayout.addLayout(self.horizontalLayout)
        VargraphiX.setCentralWidget(self.centralwidget)
        self.action = QtGui.QAction(parent=VargraphiX)
        self.action.setObjectName("action")
        self.action_2 = QtGui.QAction(parent=VargraphiX)
        self.action_2.setObjectName("action_2")

        self.retranslateUi(VargraphiX)
        QtCore.QMetaObject.connectSlotsByName(VargraphiX)

    def retranslateUi(self, VargraphiX):
        _translate = QtCore.QCoreApplication.translate
        VargraphiX.setWindowTitle(_translate("VargraphiX", "MainWindow"))
        self.open.setToolTip(_translate("VargraphiX", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.open.setWhatsThis(_translate("VargraphiX", "<html><head/><body><p align=\"justify\"><br/></p></body></html>"))
        self.open.setText(_translate("VargraphiX", "Открыть файл"))
        self.upd.setText(_translate("VargraphiX", "Обновить"))
        self.filter.setToolTip(_translate("VargraphiX", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.filter.setText(_translate("VargraphiX", "Octave"))
        self.graph2.setToolTip(_translate("VargraphiX", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.graph2.setText(_translate("VargraphiX", "2d график"))
        self.graph3.setToolTip(_translate("VargraphiX", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Microsoft PhagsPa\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.graph3.setWhatsThis(_translate("VargraphiX", "<html><head/><body><p><br/></p></body></html>"))
        self.graph3.setText(_translate("VargraphiX", "3d график"))
        self.pie.setToolTip(_translate("VargraphiX", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.pie.setText(_translate("VargraphiX", "Круговая диаграмма"))
        self.Filtrs_7.setToolTip(_translate("VargraphiX", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.Filtrs_7.setText(_translate("VargraphiX", "Столбчатая диаграмма"))
        self.action.setText(_translate("VargraphiX", "Открыть"))
        self.action_2.setText(_translate("VargraphiX", "Сохранить"))
