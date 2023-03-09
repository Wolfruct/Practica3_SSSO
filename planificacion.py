from io import open
import time


#Clase proceso
class proceso():
    nombre = ""
    tiempo = 0
    prioridad = 0

#Función para mostrar la simulación de los procesos generales
def comp(p):
    barra = ""
    print(p.nombre)
    for i in range(0,p.tiempo):
        barra = barra + "#"
        print(barra)
        time.sleep(0.35)

    return
#Función para mostrar la simulación de los procesos con RR
def comp_rr(p):
    barra = ""
    print(p.nombre)
    for i in range(0,3):
        barra = barra + "#"
        print(barra)
        p.tiempo = p.tiempo - 1
        if p.tiempo == 0:
            return True
        time.sleep(0.35)

    return


#Función para leer el archivo e iniciar los algoritmos de planificación
def read():
    procesos = []
    tiempos = []
    prioridades = []
    res = ""
    con = 0

    file = open("procesos.txt", "r")

    lines = file.readlines()

    file.close()

    #Creación de los objetos tipo proceso y registro de sus tiempos y prioridades
    for l in lines:
        aux = l.split(',')
        procesos.append(proceso())
        procesos[con].nombre = aux[0]
        procesos[con].tiempo = int(aux[1])
        procesos[con].prioridad = int(aux[2])
        tiempos.append(int(aux[1]))
        prioridades.append(int(aux[2]))
        con = con + 1

    #Ordenar tiempos y prioridades
    tiempos.sort()
    prioridades.sort()

    #Planeación FIFO (Por orden de llegada)
    print("-----------FIFO-----------")
    for p in procesos:
        comp(p)

    input(res)

    #Planeación SJF (Por tiempo)
    print("-----------SJF-----------")
    aux_o = procesos.copy()
    for i in tiempos:
        for p in aux_o:
            if p.tiempo == i:
                comp(p)
                aux_o.remove(p)

    input(res)
    
    #Planeación por prioridad
    print("-----------Prioridad-----------")
    aux_p = procesos.copy()
    for j in prioridades:
        for pr in aux_p:
            if pr.prioridad == j:
                comp(pr)
                aux_p.remove(pr)
    
    input(res)

    #Planeación por RR
    print("-----------Round Robin-----------")
    b=True
    aux_l = procesos.copy()

    l=len(aux_l)-1

    while(aux_l):
        cont = 0
        while(cont<l):
            if comp_rr(aux_l[cont]):
                aux_l.remove(aux_l[cont])
                l=len(aux_l)-1
                cont = cont - 1
            cont = cont + 1
        if comp_rr(aux_l[cont]):
                aux_l.remove(aux_l[cont])
                l=len(aux_l)-1
        
    return

read()