import sqlite3
from os import path,remove




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

    if mate not in curs.execute("""SELECT * FROM Materias""").fetchall():
        curs.execute("""INSERT INTO Materias VALUES ('{}')""".format(mate))
    if paral not in curs.execute("""SELECT paralelo FROM Paralelos WHERE materia={}""".format(mate)).fetchall():
        curs.execute("""INSERT INTO Paralelos VALUES ('{},{}')""".format(mate,paral))
    lista_clases = [clase1, clase2, clasep]
    cont=0
    for clase in lista_clases:
        dia = clase[0]
        hor_i = clase[1]
        hor_f = clase[2]
        if len(clase)!=0:
            if c!=2:
                if dia not in curs.execute("""SELECT dia FROM ClasesT WHERE materia={} AND paralelo={}""".format(mate,paral)).fetchall():
                    curs.execute("""INSERT INTO ClasesT VALUES ('{},{},{},{},{}')""".format(mate,paral,dia,hor_i,hor_f))
                else:
                    curs.execute("""UPDATE SET dia={}, hora_ini={}, hora_fin={}  WHERE materia={} AND paralelo={}""".format(dia,hor_i,hor_f,mate,paral))
            else:
                if dia not in curs.execute("""SELECT dia FROM ClasesT WHERE materia={} AND paralelo={}""".format(mate,paral)).fetchall():
                    curs.execute("""INSERT INTO ClasesT VALUES ('{},{},{},{},{}')""".format(mate,paral,dia,hor_i,hor_f))
                else:
                    curs.execute("""UPDATE SET dia={}, hora_ini={}, hora_fin={}  WHERE materia={} AND paralelo={}""".format(dia,hor_i,hor_f,mate,paral))
            
        c+=1

            



    conn.commit()
    conn.close()
    pass


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
    valid = val_dia(ingreso[0].title())
    if valid == bool:
        return False
    ingreso[0]=valid
    return ingreso

def val_dia(dia):
    if dia.startswith("Mi"):
        dia="Miércoles"
    elif  dia.startswith("S"):
        dia="Sábado"
    if dia not in dias:
        return False
    return dia


mate="materia"
conn = sqlite3.connect("registros.db")
curs = conn.cursor()
print(curs.execute("""SELECT *  FROM Materias where materia={}""".format(mate)).fetchall())


#if len(curs.execute("""SELECT materia FROM Materias where materia={}""".format(mate)).fetchall()==0):
#    curs.execute("""INSERT INTO Materias VALUES ('{}')""".format(mate))
#print(curs.execute("""SELECT * FROM Materias""").fetchall())

conn.commit()
conn.close()
