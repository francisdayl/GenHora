from PyQt5 import QtWidgets, uic
import sys


class Vent_Princ(QtWidgets.QMainWindow):
    def __init__(self):
        super(Vent_Princ, self).__init__()
        uic.loadUi("Main.ui",self)
        
        self.Bot_EditReg.clicked.connect(self.abrir_EditorReg)
    
    def abrir_EditorReg(self):
        screen2 = Vent_EditorReg()
        widget.addWidget(screen2)
        widget.setCurrentIndex(widget.currentIndex()+1)

class Vent_Asistente(QtWidgets.QMainWindow):
    def __init__(self):
        super(Vent_EditorReg,self).__init__()
        uic.loadUi("Asistente.ui",self)
        self.Bot_Sal.clicked.connect(self.reg_princ)

    def reg_princ(self):
        mainwindow = Vent_Princ()
        widget.addWidget(mainwindow)
        widget.setCurrentIndex(widget.currentIndex()+1)

class Vent_EditorReg(QtWidgets.QDialog):
    def __init__(self):
        super(Vent_EditorReg,self).__init__()
        uic.loadUi("EditorRegistros.ui",self)
        self.Bot_Sal.clicked.connect(self.reg_princ)

    def reg_princ(self):
        mainwindow = Vent_Princ()
        widget.addWidget(mainwindow)
        widget.setCurrentIndex(widget.currentIndex()+1)





app = QtWidgets.QApplication(sys.argv)
mainwindow = Vent_Princ()
secwindow = Vent_EditorReg()

widget = QtWidgets.QStackedWidget()

widget.addWidget(mainwindow)
widget.addWidget(secwindow)
widget.show()
sys.exit(app.exec_())
print("a")


