# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from Asistente import *
from EditorRegistros import *
from RegistroMaterias import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(670, 490)
        
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(670, 490))
        MainWindow.setMaximumSize(QtCore.QSize(670, 490))
        MainWindow.setBaseSize(QtCore.QSize(669, 490))
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        font.setPointSize(13)
        MainWindow.setFont(font)
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setIconSize(QtCore.QSize(4, 24))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(230, 10, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.Bot_EditReg = QtWidgets.QPushButton(self.centralwidget)
        self.Bot_EditReg.setGeometry(QtCore.QRect(60, 340, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Bot_EditReg.setFont(font)
        self.Bot_EditReg.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Bot_EditReg.setObjectName("Bot_EditReg")
        self.Bot_ElimReg = QtWidgets.QPushButton(self.centralwidget)
        self.Bot_ElimReg.setGeometry(QtCore.QRect(270, 340, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Bot_ElimReg.setFont(font)
        self.Bot_ElimReg.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Bot_ElimReg.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.Bot_ElimReg.setAutoRepeatDelay(299)
        self.Bot_ElimReg.setFlat(False)
        self.Bot_ElimReg.setObjectName("Bot_ElimReg")
        self.Bot_AsisReg = QtWidgets.QPushButton(self.centralwidget)
        self.Bot_AsisReg.setGeometry(QtCore.QRect(140, 410, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.Bot_AsisReg.setFont(font)
        self.Bot_AsisReg.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Bot_AsisReg.setObjectName("Bot_AsisReg")
        self.Bot_GenHor = QtWidgets.QPushButton(self.centralwidget)
        self.Bot_GenHor.setGeometry(QtCore.QRect(360, 410, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.Bot_GenHor.setFont(font)
        self.Bot_GenHor.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Bot_GenHor.setObjectName("Bot_GenHor")
        self.Bot_AgrReg = QtWidgets.QPushButton(self.centralwidget)
        self.Bot_AgrReg.setGeometry(QtCore.QRect(470, 340, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Bot_AgrReg.setFont(font)
        self.Bot_AgrReg.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Bot_AgrReg.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.Bot_AgrReg.setObjectName("Bot_AgrReg")
        self.Text_Hing = QtWidgets.QTextEdit(self.centralwidget)
        self.Text_Hing.setGeometry(QtCore.QRect(470, 90, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Text_Hing.setFont(font)
        self.Text_Hing.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.Text_Hing.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.Text_Hing.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.Text_Hing.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.Text_Hing.setAutoFormatting(QtWidgets.QTextEdit.AutoNone)
        self.Text_Hing.setLineWrapMode(QtWidgets.QTextEdit.WidgetWidth)
        self.Text_Hing.setLineWrapColumnOrWidth(1)
        self.Text_Hing.setReadOnly(False)
        self.Text_Hing.setTabStopWidth(2)
        self.Text_Hing.setObjectName("Text_Hing")
        self.Text_Hsal = QtWidgets.QTextEdit(self.centralwidget)
        self.Text_Hsal.setGeometry(QtCore.QRect(470, 150, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Text_Hsal.setFont(font)
        self.Text_Hsal.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.Text_Hsal.setObjectName("Text_Hsal")
        self.Text_TMax = QtWidgets.QTextEdit(self.centralwidget)
        self.Text_TMax.setGeometry(QtCore.QRect(470, 210, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Text_TMax.setFont(font)
        self.Text_TMax.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.Text_TMax.setObjectName("Text_TMax")
        self.Text_MMax = QtWidgets.QTextEdit(self.centralwidget)
        self.Text_MMax.setGeometry(QtCore.QRect(470, 270, 41, 31))
        self.Text_MMax.setMinimumSize(QtCore.QSize(0, 31))
        self.Text_MMax.setMaximumSize(QtCore.QSize(151, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Text_MMax.setFont(font)
        self.Text_MMax.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.Text_MMax.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.Text_MMax.setAutoFormatting(QtWidgets.QTextEdit.AutoNone)
        self.Text_MMax.setObjectName("Text_MMax")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(90, 90, 291, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(90, 150, 291, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(90, 200, 321, 41))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(90, 270, 291, 31))
        self.label_5.setObjectName("label_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 670, 21))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.Bot_EditReg.clicked.connect(self.abrir_EditorReg)
        self.Bot_ElimReg.clicked.connect(self.eliminarReg)
        self.Bot_AsisReg.clicked.connect(self.abrir_Asistente)
        self.Bot_GenHor.clicked.connect(self.generarHorarios)
        self.Bot_AgrReg.clicked.connect(self.abrir_AgregarReg)

    def abrir_EditorReg(self):    
        print("Edit Reg")    
        edit_r.show()
        #widget.setCurrentIndex(1)

    def eliminarReg(self):
        print("Se eliminaron los registros")

    def generarHorarios(self):
        print("Se generaron N horarios")

    def abrir_AgregarReg(self):
        #widget.setCurrentIndex(2)
        agg_r.show()
        print("Esta es la ventana para agregar registros")
    
    def abrir_Asistente(self):
        #widget.setCurrentIndex(3)
        print("Esta es la ventana para abrir el asistente de registros")
        asistente_r.show()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "GenHora - By David Yánez"))
        self.label.setText(_translate("MainWindow", "Generador de Horarios"))
        self.Bot_EditReg.setText(_translate("MainWindow", "Editar Registros"))
        self.Bot_ElimReg.setText(_translate("MainWindow", "Eliminar Registros"))
        self.Bot_AsisReg.setText(_translate("MainWindow", "Asistente de Registro"))
        self.Bot_GenHor.setText(_translate("MainWindow", "Generar Horarios"))
        self.Bot_AgrReg.setText(_translate("MainWindow", "Agregar Registros"))
        self.Text_Hing.setPlaceholderText(_translate("MainWindow", "hh:mm"))
        self.Text_Hsal.setPlaceholderText(_translate("MainWindow", "hh:mm"))
        self.Text_TMax.setPlaceholderText(_translate("MainWindow", "hh:mm"))
        self.Text_MMax.setPlaceholderText(_translate("MainWindow", "0"))
        self.label_2.setText(_translate("MainWindow", "Hora de ingreso "))
        self.label_3.setText(_translate("MainWindow", "Hora de salida"))
        self.label_4.setText(_translate("MainWindow", "Tiempo máximo de espera entre materias"))
        self.label_5.setText(_translate("MainWindow", "Cantidad máxima de materias por día"))




app = QtWidgets.QApplication(sys.argv)
main = QtWidgets.QMainWindow()
edit_r = QtWidgets.QDialog()
asistente_r = QtWidgets.QMainWindow()
agg_r = QtWidgets.QDialog()


ui_main = Ui_MainWindow()
ui_main.setupUi(main)

ui_asis= Ui_AsistenteRegistros()
ui_asis.setupUi(asistente_r)

ui_editor =  Ui_EditorRegistros()
ui_editor.setupUi(edit_r)

ui_regist = Ui_Dialog()
ui_regist.setupUi(agg_r)




main.show()
sys.exit(app.exec_())


"""
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui =Ui_AsistenteRegistros()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())"""
