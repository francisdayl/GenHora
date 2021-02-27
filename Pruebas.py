from PyQt5 import QtWidgets, uic
import sys
 
class Vent_Princ(QtWidgets.QMainWindow):
    def __init__(self):
        super(Vent_Princ, self).__init__()
        uic.loadUi("Main.ui",self)
        self.resize(480,480)        

        
        self.Bot_EditReg.clicked.connect(self.abrir_EditorReg)
        self.Bot_ElimReg.clicked.connect(self.eliminarReg)
        self.Bot_AsisReg.clicked.connect(self.abrir_Asistente)
        self.Bot_GenHor.clicked.connect(self.generarHorarios)
        self.Bot_AgrReg.clicked.connect(self.abrir_AgregarReg)
    
    def abrir_EditorReg(self):        
        widget.setCurrentIndex(1)

    def eliminarReg(self):
        print("Se eliminaron los registros")

    def generarHorarios(self):
        print("Se generaron N horarios")

    def abrir_AgregarReg(self):
        widget.setCurrentIndex(2)
        print("Esta es la ventana para agregar registros")
    
    def abrir_Asistente(self):
        widget.setCurrentIndex(3)
        print("Esta es la ventana para abrir el asistente de registros")

    

class Vent_Asistente(QtWidgets.QMainWindow):
    def __init__(self):
        super(Vent_Asistente,self).__init__()
        uic.loadUi("Asistente.ui",self)
        self.Bot_Sal.clicked.connect(self.reg_princ)

    def reg_princ(self):
        widget.setCurrentIndex(0)

class Vent_EditorReg(QtWidgets.QDialog):
    def __init__(self):
        super(Vent_EditorReg,self).__init__()
        uic.loadUi("EditorRegistros.ui",self)
        self.Bot_Sal.clicked.connect(self.reg_princ)
        
    def reg_princ(self):
        widget.setCurrentIndex(0)

class Vent_AggReg(QtWidgets.QDialog):
    def __init__(self):
        super(Vent_AggReg,self).__init__()
        uic.loadUi("RegistroMaterias.ui",self)
        self.Bot_Salir.clicked.connect(self.reg_princ)
        self.resize(480,480)
        

    def reg_princ(self):
        widget.setCurrentIndex(0)



app = QtWidgets.QApplication(sys.argv)
mainwindow = Vent_Princ()

vent_edit_reg = Vent_EditorReg()
vent_agg_regg = Vent_AggReg()
vent_asist_reg = Vent_Asistente()
mainwindow.resize(100,100)
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.addWidget(vent_edit_reg)
widget.addWidget(vent_agg_regg)
widget.addWidget(vent_asist_reg)
widget.show()
sys.exit(app.exec_())



