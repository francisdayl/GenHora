# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RegistroMaterias.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from funciones import *



class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(429, 361)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(429, 361))
        Dialog.setMaximumSize(QtCore.QSize(429, 361))
        Dialog.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        font.setPointSize(11)
        Dialog.setFont(font)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 20, 141, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 115, 101, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(30, 65, 131, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(30, 164, 101, 31))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(30, 210, 51, 21))
        self.label_5.setObjectName("label_5")
        self.Check_Prac = QtWidgets.QCheckBox(Dialog)
        self.Check_Prac.setGeometry(QtCore.QRect(240, 203, 171, 41))
        self.Check_Prac.setSizeIncrement(QtCore.QSize(0, 0))
        self.Check_Prac.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Check_Prac.setObjectName("Check_Prac")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(30, 250, 101, 31))
        self.label_6.setObjectName("label_6")
        self.Bot_Salir = QtWidgets.QPushButton(Dialog)
        self.Bot_Salir.setGeometry(QtCore.QRect(30, 310, 81, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Bot_Salir.setFont(font)
        self.Bot_Salir.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Bot_Salir.setMouseTracking(False)
        self.Bot_Salir.setObjectName("Bot_Salir")
        self.Bot_Reg = QtWidgets.QPushButton(Dialog)
        self.Bot_Reg.setGeometry(QtCore.QRect(140, 310, 131, 31))
        self.Bot_Reg.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Bot_Reg.setObjectName("Bot_Reg")
        self.Bot_Borrar = QtWidgets.QPushButton(Dialog)
        self.Bot_Borrar.setGeometry(QtCore.QRect(300, 310, 111, 31))
        self.Bot_Borrar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Bot_Borrar.setObjectName("Bot_Borrar")
        self.Text_Mat = QtWidgets.QPlainTextEdit(Dialog)
        self.Text_Mat.setGeometry(QtCore.QRect(190, 24, 221, 26))
        self.Text_Mat.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.Text_Mat.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.Text_Mat.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.Text_Mat.setObjectName("Text_Mat")
        self.Text_Par = QtWidgets.QPlainTextEdit(Dialog)
        self.Text_Par.setGeometry(QtCore.QRect(150, 70, 81, 26))
        self.Text_Par.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.Text_Par.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.Text_Par.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.Text_Par.setObjectName("Text_Par")
        self.Text_PC = QtWidgets.QPlainTextEdit(Dialog)
        self.Text_PC.setGeometry(QtCore.QRect(150, 120, 251, 26))
        self.Text_PC.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.Text_PC.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.Text_PC.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.Text_PC.setObjectName("Text_PC")
        self.Text_SC = QtWidgets.QPlainTextEdit(Dialog)
        self.Text_SC.setGeometry(QtCore.QRect(150, 170, 251, 26))
        self.Text_SC.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.Text_SC.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.Text_SC.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.Text_SC.setObjectName("Text_SC")
        self.Text_CP = QtWidgets.QPlainTextEdit(Dialog)
        self.Text_CP.setGeometry(QtCore.QRect(150, 250, 251, 26))
        self.Text_CP.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.Text_CP.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.Text_CP.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.Text_CP.setObjectName("Text_CP")
        self.Text_Pract = QtWidgets.QPlainTextEdit(Dialog)
        self.Text_Pract.setGeometry(QtCore.QRect(150, 210, 71, 26))
        self.Text_Pract.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.Text_Pract.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.Text_Pract.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.Text_Pract.setObjectName("Text_Pract")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.Bot_Salir.clicked.connect(lambda: self.borrar("Todo"))
        self.Bot_Salir.clicked.connect(lambda: Dialog.close())
        self.Bot_Reg.clicked.connect(self.guardar_reg)
        self.Bot_Borrar.clicked.connect(lambda: self.borrar("Todo"))
    
    def guardar_reg(self):
        materia = self.Text_Mat.toPlainText().strip().upper()
        paralelo = self.Text_Par.toPlainText().strip().upper()
        claset_1 = self.Text_PC.toPlainText().strip().upper()
        claset_2 = self.Text_SC.toPlainText().strip().upper()
        clasep = self.Text_CP.toPlainText().strip().upper()
        paralelo_p = self.Text_Pract.toPlainText().strip().upper()
        if self.val_campos(materia, paralelo, claset_1, claset_2, clasep, paralelo_p):
            if type(val_registro(claset_1))==list:
                claset_1=val_registro(claset_1)
            if type(val_registro(claset_2))==list:
                claset_2=val_registro(claset_2)
            if type(val_registro(clasep))==list:
                clasep=val_registro(clasep)
            registrar_info(materia,paralelo,claset_1,claset_2,clasep,paralelo_p)
            boton = QtWidgets.QMessageBox()
            boton.setWindowTitle("Información")
            boton.setIcon(QtWidgets.QMessageBox.Information)
            boton.setText("Datos Ingresados Existosamente.")
            x = boton.exec_()
            if self.Check_Prac.isChecked():                
                self.borrar("Solo Practico")
            else:
                self.borrar("Info")
        else:
            boton = QtWidgets.QMessageBox()
            boton.setWindowTitle("Error")
            boton.setIcon(QtWidgets.QMessageBox.Critical)
            boton.setText("Error en los datos ingresados.\nVerifique los campos")
            x = boton.exec_()

    
    def val_campos(self, mate, paral, clase1, clase2, clasep, paralelo_p):
        if len(mate)<2 or len(paral)==0:
            return False
        if len(clase1)==0 and len(clase2)==0 :
            return False
        
        if len(clase1)!=0:
            if type(val_registro(clase1))==bool:
                return False
        
        if len(clase2)!=0:
            if type(val_registro(clase2))==bool:
                return False
        
        if (len(paralelo_p)==0 and len(clasep)!=0) or (len(paralelo_p)!=0 and len(clasep)==0):            
            return False
        if len(clasep)!=0:
            if type(val_registro(clasep))==bool:
                return False
        
        return True
    
    def borrar(self, opc):

        if opc=="Todo":
            self.Text_Mat.clear()
            self.borrar("Info")
        elif opc=="Solo Practico":
            self.Text_CP.clear()            
            self.Text_Pract.clear()
        elif opc== "Info":
            self.Text_Par.clear()
            self.Text_PC.clear()
            self.Text_SC.clear()
            self.Check_Prac.setChecked(False)
            self.Text_CP.clear()            
            self.Text_Pract.clear()


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Registro de Materias"))
        self.label.setText(_translate("Dialog", "Nombre de la Materia"))
        self.label_2.setText(_translate("Dialog", "Primera Clase"))
        self.label_3.setText(_translate("Dialog", "Paralelo"))
        self.label_4.setText(_translate("Dialog", "Segunda Clase"))
        self.label_5.setText(_translate("Dialog", "Práctico"))
        self.Check_Prac.setText(_translate("Dialog", "Actualizar solo práctico")) 
        self.label_6.setText(_translate("Dialog", "Clase Práctica"))
        self.Bot_Salir.setText(_translate("Dialog", "Salir"))
        self.Bot_Reg.setText(_translate("Dialog", "Registrar Materia"))
        self.Bot_Borrar.setText(_translate("Dialog", "Borrar Todo"))
    
    


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
