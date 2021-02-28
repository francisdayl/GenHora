import sqlite3
from os import path,remove

dias=["Lunes", "Martes", "Miércoles", "Jueves", "Viernes","Sábado"]
cad=""
for x in range(7, 23):
        if len(str(x)) != 2:
            x = "0" + str(x)
        cad += str(x) + ":00," + str(x) + ":30,"
horas = cad.split(",")[:-1]




def crear_db():
    if not path.exists('registros.db'):
          
        conn = sqlite3.connect('registros.db')
        curs = conn.cursor()
        curs.execute('''CREATE TABLE Materias  (materia CHAR PRIMARY KEY )''')
        curs.execute('''CREATE TABLE Paralelos (materia CHAR , paralelo CHAR, PRIMARY KEY(materia,paralelo) , FOREIGN KEY (materia) REFERENCES Materias(materia) )''')
        curs.execute('''CREATE TABLE ClasesT   (materia CHAR , paralelo CHAR,  dia CHAR, hora_ini CHAR, hora_fin CHAR, PRIMARY KEY(materia,paralelo,dia), FOREIGN KEY (materia,paralelo) REFERENCES Paralelos (materia,paralelo)) ''')
        curs.execute('''CREATE TABLE Practicos (materia CHAR , paralelo CHAR, paralelop CHAR, PRIMARY KEY(materia,paralelo,paralelop) , FOREIGN KEY (materia,paralelo) REFERENCES Paralelos (materia,paralelo) ) ''')
        curs.execute('''CREATE TABLE ClasesP   (materia CHAR , paralelo CHAR, paralelop CHAR, dia CHAR, hora_ini CHAR, hora_fin CHAR, PRIMARY KEY(materia,paralelo,paralelop,dia) , FOREIGN KEY (materia,paralelo,paralelop) REFERENCES Practicos (materia, paralelo, paralelop)) ''')
        conn.commit()
        conn.close()

def registrar_info( mate, paral, clase1, clase2, clasep, paralelo_p):
    conn = sqlite3.connect("registros.db")
    curs = conn.cursor()

    if len(curs.execute("""SELECT * FROM Materias WHERE materia='{}' """.format(mate)).fetchall())==0:
        curs.execute("""INSERT INTO Materias VALUES ('{}')""".format(mate))
    lista_clases = [clase1, clase2]    
    if len(curs.execute("""SELECT paralelo FROM Paralelos WHERE materia='{}' AND paralelo='{}' """.format(mate,paral)).fetchall())==0:
        curs.execute("""INSERT INTO Paralelos VALUES ('{}','{}')""".format(mate,paral))
            
        for clase in lista_clases:
            dia = clase[0]
            hor_i = clase[1]
            hor_f = clase[2]
            if len(clase)!=0:
                if len(curs.execute("""SELECT dia FROM ClasesT WHERE materia='{}' AND paralelo='{}' AND dia='{}' """.format(mate,paral,dia)).fetchall())==0:
                    curs.execute("""INSERT INTO ClasesT VALUES ('{}','{}','{}','{}','{}')""".format(mate,paral,dia,hor_i,hor_f))
                    
    else:
        for clase in lista_clases:
            dia = clase[0]
            hor_i = clase[1]
            hor_f = clase[2]
            curs.execute("""UPDATE ClasesT SET dia='{}', hora_ini='{}', hora_fin='{}'  WHERE materia='{}' AND paralelo='{}' AND dia= '{}' """.format(dia,hor_i,hor_f,mate,paral,dia))
     
    if len(paralelo_p)!=0:
        dia = clasep[0]
        hor_i = clasep[1]
        hor_f = clasep[2]
        if len(curs.execute("""SELECT paralelop FROM Practicos WHERE materia='{}' AND paralelo='{}' AND paralelop='{}' """.format(mate,paral,paralelo_p)).fetchall())==0:
            curs.execute("""INSERT INTO Practicos VALUES ('{}','{}','{}')""".format(mate,paral,paralelo_p))
            curs.execute("""INSERT INTO ClasesP VALUES ('{}','{}','{}','{}','{}','{}')""".format(mate,paral,paralelo_p,dia,hor_i,hor_f))
        else:
            
            curs.execute("""UPDATE ClasesP SET hora_ini='{}', hora_fin='{}'  WHERE materia='{}' AND paralelo='{}' AND paralelop='{}' AND dia='{}' """.format(hor_i,hor_f,mate,paral,paralelo_p,dia))
        #if len(curs.execute("""SELECT dia FROM ClasesP WHERE materia='{}' AND paralelo='{}' AND paralelop='{}' AND dia='{}' """.format(mate,paral,paralelo_p,dia)).fetchall())==0:
           
        #else:
    conn.commit()
    conn.close()
    


def val_registro(ingreso):#Valida que el registro ingresado cumpla con el formato, devuelve un string en caso de ser valido caso contrario un False
    ingreso = ingreso.strip().split("\t")
    if len(ingreso) != 3:
        return False
    hi = ingreso[1][:5]
    hf = ingreso[2][:5]
    ingreso[1] = hi
    ingreso[2] = hf
    if hi not in horas or hf not in horas:
        return False
    if horas.index(hi)>=horas.index(hf):
        return False
    valid = val_dia(ingreso[0].strip().title())
    if type(valid) == bool:
        return False
    ingreso[0]=valid.strip()
    return ingreso

def val_dia(dia):
    if dia.startswith("Mi"):
        dia="Miércoles"
    elif  dia.startswith("S"):
        dia="Sábado"
    if dia not in dias:
        return False
    return dia.strip()

