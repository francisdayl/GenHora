import sqlite3
from os import path,remove
import pickle
from itertools import combinations
import numpy as np 
import pandas as pd

dias=["Lunes", "Martes", "Miércoles", "Jueves", "Viernes","Sábado"]

cad=""
for x in range(7, 23):
    if len(str(x)) != 2:
        x = "0" + str(x)
    cad += str(x) + ":00," + str(x) + ":30,"
horas = cad.split(",")[:-1]

horas_clase=[]
for x in range(len(horas)-1):
    horas_clase.append(horas[x]+" - "+horas[x+1])


#QUERIES SQL

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
            if len(clase)!=0:
                dia = clase[0]
                hor_i = clase[1]
                hor_f = clase[2]
                if len(curs.execute("""SELECT dia FROM ClasesT WHERE materia='{}' AND paralelo='{}' AND dia='{}' """.format(mate,paral,dia)).fetchall())==0:
                    curs.execute("""INSERT INTO ClasesT VALUES ('{}','{}','{}','{}','{}')""".format(mate,paral,dia,hor_i,hor_f))
                 
    else:
        l_clas = get_clasesT(mate,paral)
        c = 0
        for clase in lista_clases:
            if len(clase)!=0:
                dia = clase[0]
                hor_i = clase[1]
                hor_f = clase[2]
                
                curs.execute("""UPDATE ClasesT SET dia='{}', hora_ini='{}', hora_fin='{}'  WHERE materia='{}' AND paralelo='{}' AND dia= '{}' """.format(dia,hor_i,hor_f,mate,paral,l_clas[c][0]))
            c+=1
    if len(paralelo_p)!=0:
        dia = clasep[0]
        hor_i = clasep[1]
        hor_f = clasep[2]
        if len(curs.execute("""SELECT paralelop FROM Practicos WHERE materia='{}' AND paralelo='{}' AND paralelop='{}' """.format(mate,paral,paralelo_p)).fetchall())==0:
            curs.execute("""INSERT INTO Practicos VALUES ('{}','{}','{}')""".format(mate,paral,paralelo_p))
            curs.execute("""INSERT INTO ClasesP VALUES ('{}','{}','{}','{}','{}','{}')""".format(mate,paral,paralelo_p,dia,hor_i,hor_f))
        else:
            
            curs.execute("""UPDATE ClasesP SET dia='{}', hora_ini='{}', hora_fin='{}'  WHERE materia='{}' AND paralelo='{}' AND paralelop='{}' """.format(dia, hor_i,hor_f,mate,paral,paralelo_p))
        #if len(curs.execute("""SELECT dia FROM ClasesP WHERE materia='{}' AND paralelo='{}' AND paralelop='{}' AND dia='{}' """.format(mate,paral,paralelo_p,dia)).fetchall())==0:
           
        #else:
    conn.commit()
    conn.close()  

def get_materias():
    conn = sqlite3.connect('registros.db')
    curs = conn.cursor()
    materias = curs.execute("""SELECT * from MATERIAS""").fetchall()
    
    conn.commit()
    conn.close()
    l_mat = []
    for mat in materias:
        l_mat.append(mat[0])
    
    return l_mat

def get_paralelos(materia):
    conn = sqlite3.connect('registros.db')
    curs = conn.cursor()
    pars = curs.execute("""SELECT paralelo from Paralelos WHERE materia='{}' """.format(materia)).fetchall()
    conn.commit()
    conn.close()
    l_par = []
    for par in pars:
        l_par.append(par[0])
    
    return l_par

def get_practicos(materia,paralelo):
    conn = sqlite3.connect('registros.db')
    curs = conn.cursor()
    pars = curs.execute("""SELECT paralelop from Practicos WHERE materia='{}' AND paralelo='{}' """.format(materia,paralelo)).fetchall()
    conn.commit()
    conn.close()
    l_par = []
    for par in pars:
        l_par.append(par[0])
    
    return l_par

def get_clasesT(mate,para):
    lis_clas=[]
    conn = sqlite3.connect('registros.db')
    curs = conn.cursor()
    pars = curs.execute("""SELECT dia,hora_ini,hora_fin from ClasesT WHERE materia='{}' AND paralelo='{}' """.format(mate,para)).fetchall()
    for tups in pars:
        lt=[]
        for datos in tups:
            lt.append(datos)
        lis_clas.append(lt)
    conn.commit()
    conn.close()
    return lis_clas


def get_clasesP(mate,para,parap):
    lis_clas=[]
    conn = sqlite3.connect('registros.db')
    curs = conn.cursor()
    pars = curs.execute("""SELECT dia,hora_ini,hora_fin from ClasesP WHERE materia='{}' AND paralelo='{}' AND paralelop ='{}' """.format(mate,para,parap)).fetchall()
    for tups in pars:
        lt=[]
        for datos in tups:
            lt.append(datos)
        lis_clas.append(lt)
    conn.commit()
    conn.close()
    return lis_clas

def elim_materia(mate):
    conn = sqlite3.connect('registros.db')
    curs = conn.cursor()
    
    curs.execute("""DELETE FROM ClasesP WHERE materia='{}' """.format(mate))
    curs.execute("""DELETE FROM ClasesT WHERE materia='{}' """.format(mate))
    curs.execute("""DELETE FROM Paralelos WHERE materia='{}' """.format(mate))
    curs.execute("""DELETE FROM Practicos WHERE materia='{}' """.format(mate))
    curs.execute("""DELETE FROM Materias WHERE materia='{}' """.format(mate))

    conn.commit()
    conn.close()

def elim_paral(mate,paral):
    conn = sqlite3.connect('registros.db')
    curs = conn.cursor()
    
    curs.execute("""DELETE FROM ClasesP WHERE materia='{}' AND paralelo = '{}' """.format(mate,paral))
    curs.execute("""DELETE FROM ClasesT WHERE materia='{}' AND paralelo = '{}' """.format(mate,paral))
    curs.execute("""DELETE FROM Paralelos WHERE materia='{}' AND paralelo = '{}' """.format(mate,paral))
    curs.execute("""DELETE FROM Practicos WHERE materia='{}' AND paralelo = '{}' """.format(mate,paral))

    conn.commit()
    conn.close()

def elim_prac(mate,paral,paralp):
    conn = sqlite3.connect('registros.db')
    curs = conn.cursor()
    
    curs.execute("""DELETE FROM ClasesP WHERE materia='{}' AND paralelo = '{}' AND paralelop = '{}' """.format(mate,paral))
    curs.execute("""DELETE FROM Practicos WHERE materia='{}' AND paralelo = '{}'  AND paralelop = '{}' """.format(mate,paral))

    conn.commit()
    conn.close()



    
#Funciones GenHora

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
    
def borrar_registros():
    if path.exists("registros.db"):
        remove("registros.db")

def val_choque_llenar_mat(DF, clases,mate):
    for clase in clases:
        dia = clase[0]
        hor_i = clase[1]
        hor_f = clase[2]
        hori = horas_clase[horas.index(hor_i)]
        horf = horas_clase[horas.index(hor_f)-1]
        compa=DF.loc[hori:horf,dia]==""
        if compa.all():
            DF.loc[hori:horf,dia]=mate
        else:
            return False

    return DF


def get_horarios():
    horarios = {}
    conn = sqlite3.connect('registros.db')
    curs = conn.cursor()
    para_tot = curs.execute("""SELECT * FROM Paralelos""").fetchall()
    materias=get_materias()
    conn.commit()
    conn.close()
    sin_rep = []
    conta_hor = 1
    for combs in combinations(para_tot,len(materias)):
        mat_reg =[]
        for pre_h in combs:
            if pre_h[0] not in mat_reg:
                mat_reg.append(pre_h[0])
            else:
                break
        if len(mat_reg)==len(materias):
            sin_rep.append(combs)
            M = pd.DataFrame(np.empty((len(horas_clase),len(dias)),dtype=str), index=horas_clase, columns=dias, dtype='str')   
            valido=True

            for pre_h in combs:                
                #Validar materias complementarias *
                clases_t = get_clasesT(pre_h[0],pre_h[1])
                validchoque = val_choque_llenar_mat(M,clases_t,pre_h[0]+" Par: "+pre_h[1])
                
                if type(validchoque)==bool:
                    valido = False
                    break
                else:
                    M = validchoque

                pars_p = get_practicos(pre_h[0],pre_h[1]) 
                if len(pars_p)!=0:
                    for par_p in pars_p:
                        clase_p = get_clasesP(pre_h[0],pre_h[1],par_p)
                        validchoque = val_choque_llenar_mat(M,clase_p,pre_h[0]+" Par: "+pre_h[1] +" Pract: "+par_p)
                        if type(validchoque)==bool:
                            valido = False
                            break
                        else:
                            M = validchoque
            if valido:
                horarios["Horario "+str(conta_hor)]=M
                conta_hor+=1
                
    pickle.dump( horarios, open( "horarios_full.xd", "wb" ) )
    return horarios
                
def filtrar_recortar(hora_ent,hora_sal,hueco,mats_max):
    hors_filt = {}
    horarios = pickle.load( open( "horarios_full.xd", "rb" ) )
    conta = 1
    for num_h in horarios:
        horario = horarios[num_h]
        if len(hora_ent)!=0 and hora_ent!="07:00":
            cond_ent = horario.loc[:horas_clase[horas.index(hora_ent)],:]==""
            if cond_ent.all().all():
                horario = horario.drop(horas_clase[:horas_clase.index(horas_clase[horas.index(hora_ent)])])
            else:
                continue
        if len(hora_sal)!=0 and hora_sal!="22:30":
            cond_sal = horario.loc[horas_clase[horas.index(hora_sal)]:,:]==""
            if cond_sal.all().all():
                horario = horario.drop(horas_clase[horas_clase.index(horas_clase[horas.index(hora_sal)]):])
            else:
                continue
        if len(mats_max)!=0:
            mats_max = int(mats_max)
            sirve = True
            for d in dias:
                unicos = horario[d].unique()
                if "" in unicos:
                    if len(unicos)-1>mats_max:
                        sirve = False
                        break:
                if len(hueco)!=0:#Para hacer huecos
                    #Hacer huecos
            pass
            if not sirve:
                continue:        
        

        pass

    print(horarios["Horario 1"])
    pass 

#get_clases_choque()
#for i in combinations(dias,4):
#hor = {"Lunes": horas.copy(), "Martes": horas.copy()}
#hor = val_choque(hor,["Lunes","07:00","08:30"])
#print(val_choque(hor,["Lunes","07:00","08:30"]))
#print(horas_clase)
#MP = pd.DataFrame(np.empty((len(horas_clase),len(dias)),dtype=str), index=horas_clase, columns=dias, dtype='str')
#MP.fillna(42)
#MP.loc["07:00 - 07:30":"08:30 - 09:00","Lunes"]="osiosi"

#MP[MP==MP.isna()]="Hola"
#print(MP.loc["07:00 - 07:30":"09:00 - 09:30","Martes"].isna().all())
#print(MP)
#compa=MP.loc["07:00 - 07:30":"09:00 - 09:30","Lunes"]==""
#print(compa.all())
#resps=get_horarios()
#print(len(resps))
#resps.to_csv("horario.csv",index=True,encoding="cp1252")
#resps["Horario 1"].to_excel("horario.xlsx",index=True,encoding="cp1252")
#filtrar_recortar("","","","")

horarios = pickle.load( open( "horarios_full.xd", "rb" ) )
hor_1 = horarios["Horario 1"]
#hor_1.drop(columns=["Viernes"],axis=1)

#hor_1=hor_1.drop(horas_clase[:horas_clase.index("09:00 - 09:30")])
d = dias[0]
print(hor_1[d].unique())
#print(type(hor_1))



