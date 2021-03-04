import tkinter as tk
import numpy as np
import itertools as it
import pandas as pd
from os import remove
from os import path
from tkinter import messagebox
from tkinter import ttk
import pickle
from pandastable import Table, TableModel

#Programa Hecho Por David Francisco Yanez Lopez
ventana = tk.Tk()
ventana.title("Generador de Horarios - By David Yánez")
ventana.geometry("600x400")
ventana.resizable(False, False)


canvas = tk.Canvas(ventana, width=400, height=400, relief='raised')
canvas.pack()

h_ent=tk.Entry(ventana,width=20,bg="white")
canvas.create_window(80, 40, window=h_ent)

h_sal=tk.Entry(ventana,width=20,bg="white")
canvas.create_window(80, 90, window=h_sal)

m_max=tk.Entry(ventana,width=20,bg="white")
canvas.create_window(80, 140, window=m_max)

t_hueco=tk.Entry(ventana,width=20,bg="white")
canvas.create_window(80, 190, window=t_hueco)


def Gen_LD():
    d = {}
    mms = []  # Materias
    pars = []  # Paralelos
    archi = open("mpl-data/Plantilla.txt", "r", encoding="cp1252")
    for lin in archi:
        lin = lin.strip()
        if lin.startswith("Materia:"):
            mms.append(lin[8:].strip())
        elif lin.startswith('Paralelo:'):
            pars.append(lin[9:].strip())
        elif len(lin)!=0:
            sub_d = {}
            inf = lin.strip().split('-')
            sd = {}
            for p in inf:  # Creo el diccionario de inicio y fin de clase
                dats = p.split("\t")
                di = dats[0].strip()
                if di not in sd:
                    sd[di] = {"Inicio": dats[1].strip()[:5], "Fin": dats[2].strip()[:5]}
                else:

                    sd[di]["Fin"] = dats[2].strip()[:5]
            if mms[-1] not in d:
                sub_d[pars[-1]] = sd  # Agrego la informacion del paralelo
                d[mms[-1]] = sub_d  # Agrego el paralelo para la materia
            else:
                d[mms[-1]][pars[-1]] = sd
    archi.close()
    return d

def Reesc_Plant(d):
    nd = {}
    for mate in d:
        sub_d={}
        pars=sorted(list(d[mate].keys()))
        for p in pars:
            sub_d[p]=d[mate][p]
        nd[mate]=sub_d
    d=nd
    cad=""
    for mate in d:
        cad+="Materia:"+mate+"\n"
        for par in d[mate]:
            cad+="Paralelo:"+par+"\n"
            for dia in d[mate][par]:
                cad+=dia+"\t"+d[mate][par][dia]['Inicio']+"\t"+d[mate][par][dia]['Fin']+"-"
            cad=cad[:-1]+"\n"
    remove("mpl-data/Plantilla.txt")
    arch = open("mpl-data/Plantilla.txt", "w", encoding="cp1252")
    arch.write(cad[:-1])
    arch.close()
    return ""


def Leer_Dat(horaent, horasal, maxM, hueco):
    cad = ""
    for x in range(7, 23):
        if len(str(x)) != 2:
            x = "0" + str(x)
        cad += str(x) + ":00," + str(x) + ":30,"
    hrs = cad.split(",")[:-1]
    huecos = ['00:00', '00:30', '01:00', '01:30', '02:00', '02:30', '03:00', '03:30', '04:00', '04:30', '05:00',
              '05:30', '06:00', '06:30', '07:00', '07:30', '08:00', '08:30', '09:00', '09:30', '10:00', '10:30',
              '11:00', '11:30', '12:00']
    maxM = int(maxM)
    t_esp = huecos.index(hueco)
    posi = hrs.index(horaent)
    posf = hrs.index(horasal)
    hrs = hrs[posi:posf + 1]

    LH = []
    for i in range(len(hrs) - 1):
        LH.append(hrs[i] + "-" + hrs[i + 1])
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes","Sábado"]
    d = Gen_LD()
    mates = []  # Creo una lista con la materia con sus respectivos paralelos
    for m in d:
        for pa in d[m]:
            mates.append(m + "-" + pa)
    mate_comb = []  # Lista con las combinaciones entre las materias con sus paralelos
    for combi in it.combinations(mates, len(d)):  # Recorro todas las combinaciones de las materias
        c = 0
        repe = []  # Lista para las materias registradas en la combinacion para evitar repeticion de materia
        for elem in combi:
            pos = elem.index("-")
            elem = elem[:pos]  # Le quito el paralelo a la materia solo me interesa saber la materia
            if elem not in repe:  # Si no esta en la lista la guardo
                repe.append(elem)
            else:  # Caso contrario incremento el contador que me lleva la cuenta de cuantas repeticiones se dan en la combinacion
                c += 1
        if c == 0:  # Si no hubo repeticiones en las materias combinadas entonces guardo esa combinacion
            mate_comb.append(combi)
    # Horarios con combinacion pero con choque

    horarios = {}
    c1 = 1
    for comb in mate_comb:  # Recorro las tuplas de combinaciones
        hor = {"Lunes": {}, "Martes": {}, "Miércoles": {}, "Jueves": {}, "Viernes": {}}
        for mater in comb:  # Recorro las materias con paralelo de esa combinacin
            pos = mater.index("-")
            materia = mater[:pos]
            paral = mater[pos + 1:]
            for dia in d[materia][paral]:
                hor[dia][materia] = {paral: d[materia][paral][dia]}
        horarios["H" + str(c1)] = hor
        c1 += 1

    # Filtro de horarios para tener los que no chocan
    horarios_final = {}
    for h in horarios:  # Horarios con choque
        choques = 0
        for ds in horarios[h]:  # Dias del horario
            horas = hrs.copy()
            clas = horarios[h][ds]
            regs = []
            regi = []  # Horas de inicio
            regf = []  # Horas de salida
            cm=0
            if len(horarios[h][ds]) >1:
                for m in clas:
                    if list(horarios[h][ds].keys()).count(m)>1:
                        m=m+">"*cm
                        cm+=1
                    for p in clas[m]:
                        clasei = clas[m][p]["Inicio"]
                        clasef = clas[m][p]["Fin"]
                        if (clasei in hrs) and (clasef in hrs):
                            if m.endswith('*'):
                                ci = "a.a"
                                cf = "e.e"
                                if clasef == hrs[-1]:
                                    cf = hrs[hrs.index(clasef)]
                                else:
                                    cf = hrs[hrs.index(clasef) + 1]
                                if clasei == hrs[0]:
                                    ci = hrs[hrs.index(clasei)]
                                else:
                                    ci = hrs[hrs.index(clasei) - 1]
                                regs.append([ci, cf])
                                regi.append(ci)
                                regf.append(cf)
                            else:
                                regs.append([clasei, clasef])
                                regi.append(clasei)
                                regf.append(clasef)
                        else:
                            choques += 1
                if choques>0:
                    break
                if len(regi) > 1:  # Si en el dia hay mas de 1 clase
                    vregi = np.array(regi, dtype=str)
                    vregf = np.array(regf, dtype=str)
                    if (np.size(np.unique(vregi)) - np.size(vregi)) != 0:
                        choques += 1
                    if (np.size(np.unique(vregf)) - np.size(vregf)) != 0:
                        choques += 1
                    regs=sorted(regs)
                    #[['07:00', '09:00']['11:00', '13:00']]
                    for hr in regs:
                        inds = []
                        for hp in hr:
                            if hp in horas:
                                inds.append(horas.index(hp))
                            else:
                                choques += 1
                                break

                        if len(inds) == 2:
                            for i in range(inds[0], inds[1]):
                                horas[i] = '0'

        if choques == 0:
            horarios_final[h] = horarios[h]


    horariosF = {}
    for h in horarios_final:
        cm = 0
        for ds in horarios_final[h]:
            if len(horarios_final[h][ds]) > maxM:
                cm += 1
                break
        if cm == 0:
            ht = {}
            dt = horarios_final[h]
            for ds in dt:
                dt2 = {}
                dic_ds = dt[ds]
                for mats in dic_ds:
                    clav = list(dic_ds[mats].keys())[0]
                    dt2[mats + "-P" + clav] = dic_ds[mats][clav]
                ht[ds] = dt2
            horariosF[h] = ht
    df = {}
    lis_df = []
    for h in horariosF:
        M2 = np.empty((len(LH), len(dias)), dtype='str')
        MP = pd.DataFrame(M2, index=LH, columns=dias, dtype='str')
        hf = horariosF[h]
        for ds in hf:
            for m in hf[ds]:
                ini = hf[ds][m]["Inicio"]
                fin = hf[ds][m]["Fin"]
                MP.loc[ini:fin, ds] = m.strip()
        esta = 1
        M = MP.to_numpy()

        for y in range(len(dias)):
            fila = M[:, y]
            unis = np.unique(fila)
            if np.size(unis) >= 3:
                l_uni = []
                l = []
                for i in fila:
                    i = i.strip()
                    l.append(i.strip())
                    if len(i) != 0 and i not in l_uni:
                        l_uni.append(i)
                for i in range(len(l_uni) - 1):
                    ele_i = l_uni[i]
                    ele_f = l_uni[i + 1]
                    ind_i = l.index(ele_i)
                    ind_f = l.index(ele_f)
                    if l[ind_i:ind_f + 1].count("") > t_esp:
                        esta = 0

        if esta == 1:
            lis_df.append(MP)
            df[h] = {1: hf, 2: M}
    ab=open("horariobin","wb")
    pickle.dump(lis_df,ab)
    ab.close()
    return (df, LH, dias)





def EscDat(df, LH, dias):
    arch = open("Horarios.csv", "w", encoding="cp1252")
    cf = 2
    cad = " ;Lunes;Martes;Miércoles;Jueves;Viernes\n"
    for h in df:
        hf = df[h]
        M = hf[2]
        for x in range(len(LH)):
            fil = LH[x] + ";"
            for y in range(len(dias)):
                fil += M[x, y].strip() + ";"
            fil += "\n"
            cad += fil
        if cf < len(df) + 1:
            cad += "\n\n;;;" + "Horario " + str(cf) + " ;;\n\n"
        cf += 1
    arch.write(cad.replace(">",""))
    arch.close()

    return ""

def ValUni(infor, dias, horas):
    ce = 0
    try:
        lis = infor.strip().split("\t")
        dia = lis[0].strip()
        ini = lis[1].strip()
        fin = lis[2].strip()
        if dia not in dias:
            if dia[:-1] not in dias:
                ce += 1
        if ini[:5] not in horas:
            ce += 1
        if fin[:5] not in horas:
            ce += 1
    except:
        ce+=1
        return ce
    return ce

def ValHor(info):
    dias=["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
    cad = ""
    for x in range(7, 23):
        if len(str(x)) != 2:
            x = "0" + str(x)
        cad += str(x) + ":00," + str(x) + ":30,"
    horas = cad.split(",")[:-1]
    cf = 0
    try:
        if "-" in info:
            lis = info.split("-")
            for inf in lis:
                cf += ValUni(inf,dias,horas)
        else:
            cf += ValUni(info,dias,horas)
    except:
        cf += 1
    return cf


def prob_maxM():
    msj_sal = tk.Label(ventana, text='Ingrese hasta que hora desea usted\n terminar sus clases con el formato (hh:mm)')
    canvas.create_window(300, 90, window=msj_sal)
    msj_max = tk.Label(ventana, text='Ingrese hasta cuantas\nmaterias desea ver por dia')
    canvas.create_window(300, 140, window=msj_max)
    msj_hueco = tk.Label(ventana,
                         text='Ingrese hasta cuanto tiempo esperaria\npara ver una materia tras otra con el formato (hh:mm)')
    canvas.create_window(300, 190, window=msj_hueco)
    cad = ""
    for x in range(7, 23):
        if len(str(x)) != 2:
            x = "0" + str(x)
        cad += str(x) + ":00," + str(x) + ":30,"
    hrs = cad.split(",")[:-1]
    ejecu = True
    horaent = h_ent.get().strip()
    if len(horaent)==0:
        horaent =hrs[0]
    horasal = h_sal.get().strip()
    if len(horasal)==0:
        horasal=hrs[-1]
    maxM = m_max.get().strip()
    if len(maxM)==0:
        maxM=str(len(Gen_LD()))
    hueco = t_hueco.get().strip()
    if len(hueco)==0:
        hueco="12:00"
    if horaent not in hrs:
        label1 = tk.Label(ventana, text='Hora no valida', font=('helvetica', 10))
        canvas.create_window(80, 65, window=label1)
        ejecu = False
    else:
        label1 = tk.Label(ventana, text='                        ', font=('helvetica', 10))
        canvas.create_window(80, 65, window=label1)

    val = False
    if horasal in hrs:
        if hrs.index(horasal) <= hrs.index(horaent):
            val = True
            ejecu = False
    if (horasal not in hrs) or val:
        label2 = tk.Label(ventana, text='Hora no valida', font=('helvetica', 10))
        canvas.create_window(80, 115, window=label2)
        ejecu = False
    else:
        label2 = tk.Label(ventana, text='                    ', font=('helvetica', 10))
        canvas.create_window(80, 115, window=label2)
    if not maxM.isdigit():
        label3 = tk.Label(ventana, text='Error de Ingreso', font=('helvetica', 10))
        canvas.create_window(80, 165, window=label3)
        ejecu=False
    else:
        label3 = tk.Label(ventana, text='                            ', font=('helvetica', 10))
        canvas.create_window(80, 165, window=label3)
    huecos = ['00:00', '00:30', '01:00', '01:30', '02:00', '02:30', '03:00', '03:30', '04:00', '04:30', '05:00', '05:30', '06:00', '06:30', '07:00', '07:30', '08:00', '08:30', '09:00', '09:30', '10:00','10:30', '11:00', '11:30', '12:00']
    if hueco not in huecos:
        label4 = tk.Label(ventana, text='Error de Ingreso', font=('helvetica', 10))
        canvas.create_window(80, 215, window=label4)
        ejecu = False
    else:
        label4 = tk.Label(ventana, text='                           ', font=('helvetica', 10))
        canvas.create_window(80, 215, window=label4)
    if ejecu:
        if path.exists("mpl-data/Plantilla.txt"):
            try:
                df,LH,dias=Leer_Dat(horaent, horasal, maxM, hueco)
                if len (df)==0:
                    tk.messagebox.showerror(title="Error",
                                            message="No se pudieron generar horarios que cumplan con sus requerimientos, cambie sus parámetros"
                                                    )
                else:
                    escr = EscDat(df, LH, dias)
                    tk.messagebox.showinfo(title="GenHora",message=str(len(df))+" Horarios Generados Exitosamente")
                    lit_d=Gen_LD()
                    try:
                        ab = open("registrosbin", "wb")
                        pickle.dump([], ab)
                        ab.close()
                    except:

                        pass

            except:
                tk.messagebox.showerror(title="Error",message="Eror en la creación de horarios, Verifique registros o Cree nuevos registros")
        else:
            tk.messagebox.showerror(title="Error", message="No existen registros para generar horarios")
    else:
        label6 = tk.Label(ventana, text="                                                  "*30, font=('helvetica', 10))
        canvas.create_window(200, 345, window=label6)

    return ""


def Carg_dat():

    def Limpiar2():
        val_mat.delete(first=0, last=400)
        val_par.delete(first=0, last=400)
        val_dia1.delete(first=0, last=400)
        val_dia2.delete(first=0, last=400)
        val_dia3.delete(first=0, last=400)
        msj_car = tk.Label(sub_v, text='                                                        ')
        canvas2.create_window(200, 290, window=msj_car)
        msj_err = tk.Label(sub_v, text='                                          ')
        canvas2.create_window(290, 91, window=msj_err)
        return ""

    def Salir():
        sub_v.destroy()
        return

    def proc_inf():
        cerr=0
        dia1=val_dia1.get().strip()
        dia2=val_dia2.get().strip()
        dia3=val_dia3.get().strip()
        cade=""
        if len(dia1)!=0:
            if ValHor(dia1)>0:
                cerr+=1
            else:
                cade+=dia1+"-"

        if len(dia2)!=0:
            if ValHor(dia2)>0:
                cerr+=1
            else:
                cade+=dia2+"-"

        if len(dia3)!=0:
            if ValHor(dia3)>0:
                cerr+=1
            else:
                cade+=dia3+"-"
        para=val_par.get().strip()
        dest=0
        if not para.isdigit():
            msj_err = tk.Label(sub_v, text='Ingrese Paralelo Válido')
            canvas2.create_window(290, 91, window=msj_err)
            cerr+=1
            dest=1
        else:
            mater="Materia:"+val_mat.get().strip()
            paral="Paralelo:"+para
            if len(val_mat.get().strip())>2 and cerr==0 :
                Cad_Fin="\n{}\n{}\n{}".format(mater,paral,cade[:-1])
                archi=open("mpl-data/Plantilla.txt", "a",encoding="cp1252")
                archi.write(Cad_Fin)
                archi.close()
                tk.messagebox.showinfo(title="Datos Guardados",message="Datos Guardados exitosamente")
                a=Reesc_Plant(Gen_LD())
                val_dia1.delete(first=0, last=400)
                val_dia2.delete(first=0, last=400)
                val_dia3.delete(first=0, last=400)
                val_par.delete(first=0, last=400)
                msj_err = tk.Label(sub_v, text='                                          ')
                canvas2.create_window(290, 91, window=msj_err)
                sub_v.attributes('-topmost', 1)
            else:
                if dest==0:
                    msj_err = tk.Label(sub_v, text='                                          ')
                    canvas2.create_window(290, 91, window=msj_err)
                a=tk.messagebox.showerror(title="Error de ingreso",message="Verifique y corrija la informacion ingresada")
                sub_v.attributes('-topmost', 1)
        sub_v.attributes('-topmost', 0)

    sub_v = tk.Tk()
    sub_v.title("Registrador de Datos")
    sub_v.geometry("470x320")
    canvas2 = tk.Canvas(sub_v, width=400, height=320, relief='raised')
    msj_mat = tk.Label(sub_v, text='Ingrese el nombre de la materia:')
    canvas2.create_window(100, 40, window=msj_mat)
    val_mat = tk.Entry(sub_v, width=30, bg="white")
    canvas2.create_window(290, 40, window=val_mat)

    msj_par = tk.Label(sub_v, text='Ingrese el paralelo:')
    canvas2.create_window(65, 70, window=msj_par)
    val_par = tk.Entry(sub_v, width=10, bg="white")
    canvas2.create_window(230, 70, window=val_par)

    msj_dia1 = tk.Label(sub_v, text='Ingrese el horario del 1er día:')
    canvas2.create_window(91, 120, window=msj_dia1)
    val_dia1 = tk.Entry(sub_v, width=34, bg="white")
    canvas2.create_window(290, 120, window=val_dia1)

    msj_dia2 = tk.Label(sub_v, text='Ingrese el horario del 2do día:')
    canvas2.create_window(91, 150, window=msj_dia2)
    val_dia2 = tk.Entry(sub_v, width=34, bg="white")
    canvas2.create_window(290, 150, window=val_dia2)

    msj_dia3 = tk.Label(sub_v, text='Ingrese el horario del 3er día:')
    canvas2.create_window(91, 180, window=msj_dia3)

    val_dia3 = tk.Entry(sub_v, width=34, bg="white")
    canvas2.create_window(290, 180, window=val_dia3)

    bot_limp2 = tk.Button(sub_v, text="Limpiar Todo", command=Limpiar2, fg="black", font="arial 10")
    canvas2.create_window(50, 250, window=bot_limp2)

    bot_carg = tk.Button(sub_v, text="Cargar Datos", command=proc_inf, fg="black", font="arial 10")
    canvas2.create_window(220, 250, window=bot_carg)

    bot_sal = tk.Button(sub_v, text="Salir", command=Salir, fg="black", font="arial 10")
    canvas2.create_window(375, 250, window=bot_sal)

    sub_v.geometry("+{}+{}".format(430, 200))
    canvas2.pack()
    pass

def Adv_Bor():
    if not path.exists("mpl-data/Plantilla.txt"):
        messagebox.showinfo(title="Notificacion",message="No existen datos por borrar")
    else:
        val=messagebox.askyesno(title="Mensaje de Advertencia",message="¿Desea borrar los datos registrados?")
        if val==1:
            remove("mpl-data/Plantilla.txt")
            messagebox.showinfo(title="Notificacion", message="Datos Previos Borrados Exitosamente")
    return " "

def Ver_Reg():
    if not path.exists("mpl-data/Plantilla.txt"):
        messagebox.showerror(title="Error",message="No existen registros para mostrar")
    else:

        def actualizar_entry(acc):
            palab = acc.widget.get()
            palab = palab.strip().lower()
            lis_temp = []
            if palab == "":
                lis_temp = list(d.keys())
            else:
                for mate in list(d.keys()):
                    if palab in mate.lower():
                        lis_temp.append(mate)
            lis_box.delete(0, 'end')
            lis_temp = sorted(lis_temp, key=str.lower)
            lis_box.insert('end', *lis_temp)


        def Gen_Combo(selec):
            def Elim_mat():
                root.attributes('-topmost', 0)
                try:
                    if palab not in d:
                        root.attributes('-topmost', 0)
                        tk.messagebox.showerror(title="Error", message="La materia no existe")
                        root.attributes('-topmost', 1)
                    else:
                        root.attributes('-topmost', 0)
                        val = tk.messagebox.askyesno(title="Borrar materia", message="¿Desea borrar {}?".format(palab))
                        root.attributes('-topmost', 1)
                        if val == 1:
                            root.attributes('-topmost', 0)
                            tapa_ent = tk.Frame(root, width=550, height=125, bg="#f0f0f0")
                            canvas.create_window(300, 200, window=tapa_ent)
                            del d[palab]
                            ent_mat.delete(0, 'end')
                            lis_box.delete(0, 'end')
                            lis_temp = sorted(list(d.keys()), key=str.lower)
                            lis_box.insert('end', *lis_temp)
                            comb.destroy()
                            root.attributes('-topmost', 0)
                            tk.messagebox.showinfo(title="Materia Eliminada",
                                                   message="{} Fue Eliminado Exitosamente".format(palab))
                            a = Reesc_Plant(d)
                            root.attributes('-topmost',1)

                except:
                    cc=0
            bot_elm = tk.Button(root, text=" Eliminar Materia", fg="black", font="arial 10", command=Elim_mat)
            canvas.create_window(115, 310, window=bot_elm)

            try:
                def Mostrar_Infpar(even):
                    root.attributes('-topmost', 0)
                    mate_ent=ent_mat.get().strip()
                    if palab!="":
                        if mate_ent in list(d.keys()):
                            tapa_ent=tk.Frame(root,width=400,height=90,bg="#f0f0f0")
                            canvas.create_window(300,240,window=tapa_ent)
                            paral=comb.selection_get()
                            if paral in d[mate_ent]:
                                mat_par = tk.Label(root, text="{} Paralelo: {}".format(mate_ent , paral), fg="black",
                                                   font="arial 14",width=50)
                                canvas.create_window(300,150,window=mat_par)
                                hor_mat_par=list(d[mate_ent][paral].keys())

                                dia=tk.Label(root, text="Día", fg="black",
                                                   font="arial 12")
                                canvas.create_window(190,180,window=dia)

                                inic = tk.Label(root, text="Hora Inicio", fg="black",
                                               font="arial 12")
                                canvas.create_window(315, 180, window=inic)

                                fin = tk.Label(root, text="Hora Fin", fg="black",
                                               font="arial 12")
                                canvas.create_window(440, 180, window=fin)

                                if len(hor_mat_par)==3:

                                    dia1 = hor_mat_par[0]
                                    hors_dia1=d[mate_ent][paral][dia1]
                                    d1 = tk.Entry(root, width=10)
                                    d1.insert(0, dia1)
                                    canvas.create_window(190, 210, window=d1)

                                    ent_d1=tk.Entry(root, width=10)
                                    ent_d1.insert(0, hors_dia1["Inicio"])
                                    canvas.create_window(315, 210, window=ent_d1)

                                    sal_d1=tk.Entry(root, width=10)
                                    sal_d1.insert(0, hors_dia1["Fin"])
                                    canvas.create_window(440, 210, window=sal_d1)


                                    dia2 = hor_mat_par[1]
                                    hors_dia2 = d[mate_ent][paral][dia2]
                                    d2 = tk.Entry(root, width=10)
                                    d2.insert(0, dia2)
                                    canvas.create_window(190, 230, window=d2)

                                    ent_d2 = tk.Entry(root, width=10)
                                    ent_d2.insert(0, hors_dia2["Inicio"])
                                    canvas.create_window(315, 230, window=ent_d2)

                                    sal_d2 = tk.Entry(root, width=10)
                                    sal_d2.insert(0, hors_dia2["Fin"])
                                    canvas.create_window(440, 230, window=sal_d2)


                                    dia3 = hor_mat_par[2]
                                    hors_dia3 = d[mate_ent][paral][dia3]
                                    d3 = tk.Entry(root, width=10)
                                    d3.insert(0, dia3)
                                    canvas.create_window(190, 250, window=d3)

                                    ent_d3 = tk.Entry(root, width=10)
                                    ent_d3.insert(0, hors_dia3["Inicio"])
                                    canvas.create_window(315, 250, window=ent_d3)

                                    sal_d3 = tk.Entry(root, width=10)
                                    sal_d3.insert(0, hors_dia3["Fin"])
                                    canvas.create_window(440, 250, window=sal_d3)

                                elif len(hor_mat_par)==2:
                                    dia1 = hor_mat_par[0]
                                    hors_dia1 = d[mate_ent][paral][dia1]
                                    d1 = tk.Entry(root, width=10)
                                    d1.insert(0, dia1)
                                    canvas.create_window(190, 210, window=d1)

                                    ent_d1 = tk.Entry(root, width=10)
                                    ent_d1.insert(0, hors_dia1["Inicio"])
                                    canvas.create_window(315, 210, window=ent_d1)

                                    sal_d1 = tk.Entry(root, width=10)
                                    sal_d1.insert(0, hors_dia1["Fin"])
                                    canvas.create_window(440, 210, window=sal_d1)

                                    dia2 = hor_mat_par[1]
                                    hors_dia2 = d[mate_ent][paral][dia2]
                                    d2 = tk.Entry(root, width=10)
                                    d2.insert(0, dia2)
                                    canvas.create_window(190, 230, window=d2)

                                    ent_d2 = tk.Entry(root, width=10)
                                    ent_d2.insert(0, hors_dia2["Inicio"])
                                    canvas.create_window(315, 230, window=ent_d2)

                                    sal_d2 = tk.Entry(root, width=10)
                                    sal_d2.insert(0, hors_dia2["Fin"])
                                    canvas.create_window(440, 230, window=sal_d2)


                                elif len(hor_mat_par)==1:
                                    dia1 = hor_mat_par[0]
                                    hors_dia1 = d[mate_ent][paral][dia1]
                                    d1 = tk.Entry(root, width=10)
                                    d1.insert(0, dia1)
                                    canvas.create_window(190, 210, window=d1)

                                    ent_d1 = tk.Entry(root, width=10)
                                    ent_d1.insert(0, hors_dia1["Inicio"])
                                    canvas.create_window(315, 210, window=ent_d1)

                                    sal_d1 = tk.Entry(root, width=10)
                                    sal_d1.insert(0, hors_dia1["Fin"])
                                    canvas.create_window(440, 210, window=sal_d1)

                                def Elim_par():
                                    try:
                                        if paral in d[mate_ent]:
                                            if len(d[mate_ent])==1:
                                                a=Elim_mat()
                                            else:
                                                root.attributes('-topmost', 0)
                                                val = tk.messagebox.askyesno(title="Borrar paralelo",
                                                                             message="¿Desea eliminar el paralelo {}?".format(
                                                                                 paral))
                                                root.attributes('-topmost', 1)
                                                if val==1:
                                                    del d[mate_ent][paral]
                                                    tapa_ent = tk.Frame(root, width=550, height=125, bg="#f0f0f0")
                                                    canvas.create_window(300, 200, window=tapa_ent)
                                                    root.attributes('-topmost', 0)
                                                    tk.messagebox.showinfo(title="Paralelo Eliminado",
                                                                                    message="El Paralelo {} de {} Fue Eliminado Exitosamente".format(
                                                                                        paral,mate_ent))
                                                    a=Reesc_Plant(d)
                                                    root.attributes('-topmost', 1)

                                        else:
                                            root.attributes('-topmost', 0)
                                            tk.messagebox.showerror(title="Error",message="No se ha encontrado el paralelo")
                                            root.attributes('-topmost', 1)
                                    except:
                                        cc=0

                                def Guard_Camb():
                                    lins=[0,0,0]
                                    ds=[]
                                    semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
                                    dias_reg=[]
                                    try:
                                        if str(d1.get().strip()) in semana:
                                            dias_reg.append(str(d1.get().strip()))
                                            lins[0]+=1
                                    except:
                                        lins[0] += 0

                                    try:
                                        if str(d2.get().strip()) in semana:
                                            lins[1]+=1
                                            dias_reg.append(str(d1.get().strip()))
                                    except:
                                        lins[1] += 0

                                    try:
                                        if str(d3.get().strip()) in semana:
                                            lins[2]+=1
                                            dias_reg.append(str(d1.get().strip()))
                                    except:
                                        lins[2] += 0


                                    cad=""
                                    if lins[0]>0:
                                        cad+="{}\t{}\t{}-".format(d1.get().strip().title(),ent_d1.get().strip(),sal_d1.get().strip())
                                    if lins[1] > 0:
                                        cad+= "{}\t{}\t{}-".format(d2.get().strip().title(), ent_d2.get().strip(),
                                                                   sal_d2.get().strip())
                                    if lins[2] > 0:
                                        cad+= "{}\t{}\t{}-".format(d3.get().strip().title(), ent_d3.get().strip(),
                                                                   sal_d3.get().strip())


                                    err=ValHor(cad[:-1])
                                    if err==0 and len(d[mate_ent][paral]) == sum(lins):
                                        root.attributes('-topmost', 0)
                                        val=tk.messagebox.askyesno(title="Guardar Cambios",
                                                               message="¿Desea cambiar el registro del paralelo {}?".format(paral))
                                        root.attributes('-topmost', 1)
                                        if val == 1:
                                            if len(d[mate_ent][paral])==1:
                                                d[mate_ent][paral]={d1.get().strip():{"Inicio":ent_d1.get().strip(),"Fin":sal_d1.get().strip()}}
                                            elif len(d[mate_ent][paral])==2:
                                                d[mate_ent][paral] = {d1.get().strip(): {"Inicio": ent_d1.get().strip(),
                                                                                        "Fin": sal_d1.get().strip()},d2.get().strip(): {"Inicio": ent_d2.get().strip(),
                                                                                        "Fin": sal_d2.get().strip()}}
                                            elif len(d[mate_ent][paral])==3:
                                                d[mate_ent][paral] = {d1.get().strip(): {"Inicio": ent_d1.get().strip(),
                                                                                        "Fin": sal_d1.get().strip()},

                                                                     d2.get().strip(): {"Inicio": ent_d2.get().strip(),
                                                                                        "Fin": sal_d2.get().strip()},d3.get().strip():{"Inicio":ent_d3.get().strip(),"Fin":sal_d3.get().strip()}}
                                            a = Reesc_Plant(d)
                                            tapa_ent = tk.Frame(root, width=550, height=125, bg="#f0f0f0")
                                            canvas.create_window(300, 200, window=tapa_ent)
                                            root.attributes('-topmost', 0)
                                            tk.messagebox.showinfo(title="Guardar Cambios",message="Cambios Guardados Exitosamente")
                                            root.attributes('-topmost', 1)
                                    else:
                                        root.attributes('-topmost', 0)
                                        tk.messagebox.showerror(title="Error",message="Error al cargar los datos, Verificar los cambios")
                                        root.attributes('-topmost', 1)

                                bot_elp=tk.Button(root,text=" Eliminar Paralelo ",fg="black",font="arial 10",command=Elim_par)
                                canvas.create_window(295,310,window=bot_elp)
                                bot_guar = tk.Button(root, text=" Guardar Cambios ",fg="black",font="arial 10",command=Guard_Camb)
                                canvas.create_window(470, 310, window=bot_guar)
                        else:
                            comb.destroy()
                    else:
                        comb.destroy()

                root.attributes('-topmost', 0)
            except:
                t=0


            try:
                selec_lis = str(selec.widget.get(selec.widget.curselection()))
                ent_mat.delete(0, 'end')
                ent_mat.insert(0, selec_lis)
            except:
                cc=0
            palab = ent_mat.get().strip()
            lis_temp = [palab]
            lis_box.delete(0, 'end')
            lis_box.insert('end', *lis_temp)

            msj_par = tk.Label(root, text="Seleccione un paralelo:")
            canvas.create_window(430, 30, window=msj_par)

            comb = ttk.Combobox(canvas,width=4,values=list(d[palab].keys()),height=5)
            canvas.create_window(530,30,window=comb)

            comb.bind("<<ComboboxSelected>>",Mostrar_Infpar)
            #root.attributes('-topmost', 0)


        root = tk.Tk()

        root.title("Visor de Registros")
        root.geometry("600x350")
        root.resizable(False, False)
        canvas = tk.Canvas(root, width=600, height=350, relief='raised')
        d = Gen_LD()
        materias = list(d.keys())
        lis_box = tk.Listbox(canvas, height=5, width=30)
        lis_box.insert('end', *materias)
        lis_box.bind('<<ListboxSelect>>',Gen_Combo)
        canvas.create_window(255, 87, window=lis_box)

        msj_bus = tk.Label(root, text="Ingrese Materia a Buscar: ")
        canvas.create_window(90, 30, window=msj_bus)

        ent_mat = tk.Entry(root, width=30)
        canvas.create_window(255, 30, window=ent_mat)
        ent_mat.bind("<KeyRelease>", actualizar_entry)

        canvas.pack()
        root.geometry("+{}+{}".format(340, 150))
        root.mainloop()

def asis_reg():
    sub_ven = tk.Tk()
    sub_ven.title("Asistente de Registros ")
    sub_ven.geometry("660x600")
    canv = tk.Canvas(sub_ven, width=660, height=600, relief='raised')


    #msj_el.config(text="dad")


    mat_reg=tk.Entry(sub_ven,width=30,bg="white")
    canv.create_window(300, 420, window=mat_reg)


    canv.create_window(100, 420, window=tk.Label(sub_ven, text='Ingrese Materia Registrada',  font="arial 11"))

    canv.create_window(530, 420, window=tk.Label(sub_ven, text='Materias Registradas', font="arial 11"))

    fram = tk.Frame(sub_ven, width=660, height=400, bg="#f0f0f0")
    global n_hor
    global horarios_df
    n_hor=0

    horarios_df=pickle.load(open("horariobin", "rb"))

    cant_hor=len(horarios_df)
    msj_el = tk.Label(sub_ven, text='Horario '+str(n_hor+1)+" de "+str(cant_hor), fg="black", font="arial 14")
    canv.create_window(330, 20, window=msj_el)

    try:
        lis_box = tk.Listbox(canv, height=5, width=25)
        lis_box.insert('end', *pickle.load(open("registrosbin", "rb")))
        canv.create_window(535, 480, window=lis_box)
    except:
        lis_box = tk.Listbox(canv, height=5, width=25)
        lis_box.insert('end', [])
        canv.create_window(535, 480, window=lis_box)

        ab = open("registrosbin", "wb")
        pickle.dump([], ab)
        ab.close()

    def most_hor(fram,conta):
        try:


            df = horarios_df[conta]
            print(df)
            table = pt = Table(fram, dataframe=df)
            table.showIndex()
            pt.show()
            canv.create_window(330, 200, window=fram)

            sub_ven.geometry("+{}+{}".format(430, 200))
            canv.pack()
        except:
            print()
        pass

    most_hor(fram,n_hor)

    def sig_hor():
        global n_hor
        n_hor += 1
        fram.destroy()
        try:
            if n_hor<=cant_hor:
                msj_el.config(text='Horario '+str(n_hor)+" de "+str(cant_hor))
                msj_el.update()
                frame = tk.Frame(sub_ven, width=660, height=400, bg="#f0f0f0")
                most_hor(frame,n_hor)
            else:
                tk.messagebox.showerror(title="Error", message="No existen Horarios siguientes")
                n_hor -= 1

        except:
            tk.messagebox.showerror(title="Error", message="No existen Horarios siguientes")
            n_hor -= 1

        pass

    def ant_hor():
        global n_hor
        n_hor -= 1
        fram.destroy()
        try:
            if n_hor < 1:
                msj_el.config(text='Horario ' + str(n_hor) + " de " + str(cant_hor))
                msj_el.update()
                frame = tk.Frame(sub_ven, width=660, height=400, bg="#f0f0f0")
                most_hor(frame, n_hor)
            else:
                tk.messagebox.showerror(title="Error", message="No existen Horarios anteriores")
                n_hor += 1
        except:
            tk.messagebox.showerror(title="Error", message="No existen Horarios anteriores" )
            n_hor+=1

        pass
    def reg_mat():
        global horarios_df
        matxreg=mat_reg.get().strip()
        n_hors=[]
        cd=0
        for hor_df in horarios_df:
            hor_mat=hor_df.to_numpy()

            try:
                if np.any(hor_mat==matxreg):
                    n_hors.append(hor_df)
                else:
                    cd += 1
                    print(cd)
            except:
                cd+=1
                print(cd)

        horarios_df=n_hors

        ab = open("horariobin", "wb")
        pickle.dump(n_hors, ab)
        ab.close()

        lis_regs = pickle.load(open("registrosbin", "rb"))
        lis_regs.append(matxreg)
        ab = open("registrosbin", "wb")
        pickle.dump(lis_regs, ab)
        ab.close()


        sub_ven.destroy()
        asis_reg()
        pass
    pass



    bot_atr = tk.Button(sub_ven, text="Horario Anterior", command=ant_hor, fg="black", font="arial 10")
    canv.create_window(70,20, window=bot_atr)
    bot_sig = tk.Button(sub_ven, text="Horario Siguiente", command=sig_hor, fg="black", font="arial 10")
    canv.create_window(580, 20, window=bot_sig)
    bot_reg = tk.Button(sub_ven, text="Registrar Materia", command=reg_mat, fg="black", font="arial 10")
    canv.create_window(180, 460, window=bot_reg)

    pass

msj_ent=tk.Label(ventana, text='Ingrese a que hora desea usted empezar\n sus clases con el formato (hh:mm)')
canvas.create_window(300, 40, window=msj_ent)
msj_sal=tk.Label(ventana, text='Ingrese hasta que hora desea usted\n terminar sus clases con el formato (hh:mm)')
canvas.create_window(300, 90, window=msj_sal)
msj_max=tk.Label(ventana, text='Ingrese hasta cuantas\nmaterias desea ver por dia')
canvas.create_window(300, 140, window=msj_max)
msj_hueco=tk.Label(ventana, text='Ingrese hasta cuanto tiempo esperaria\npara ver una materia tras otra con el formato (hh:mm)')
canvas.create_window(300, 190, window=msj_hueco)



bot_dat=tk.Button(ventana,text="Agregar Registros",command=Carg_dat,fg="black",font="arial 10")
canvas.create_window(0, 300, window=bot_dat)


bot_ver=tk.Button(ventana,text="Editar Registros",command=Ver_Reg,fg="black",font="arial 10")
canvas.create_window(130,300,window=bot_ver)

bot_nd=tk.Button(ventana,text="Borrar Registros Anteriores",command=Adv_Bor,fg="black",font="arial 10")
canvas.create_window(280, 300, window=bot_nd)

bot_ent=tk.Button(ventana,text="Generar Horarios",command=prob_maxM,fg="black",font="arial 10")
canvas.create_window(430, 300, window=bot_ent)

bot_asis=tk.Button(ventana,text="Asistente de Registros",command=asis_reg,fg="black",font="arial 10")
canvas.create_window(200, 350, window=bot_asis)

ventana.attributes('-topmost', 0)
ventana.geometry("+{}+{}".format(340, 150))

ventana.mainloop()


#Programa Hecho Por David Francisco Yanez Lopez
__author__ = "David Francisco Yanez Lopez"
__copyright__ = "Copyright (C) 2020 David Francisco Yanez Lopez"
__version__ = "5.0"

