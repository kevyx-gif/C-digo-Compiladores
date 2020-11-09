#!/usr/bin/env python
#-*-coding utf:-8-*-

class subconjunto :
    def __init__ (self, lista, marca):
        self.lista = lista
        self.marca = marca
    def show (self):
        print (self.lista, self.marca)
    def __repr__ (self):
        return str (self.lista)  

class tranSub :
    def __init__ (self, origen, destino, costo):
        self.origen = origen
        self.destino = destino
        self.costo  = costo
    def __repr__ (self):
        return str (self.origen) + "--" + str (self.costo) + "--" + str(self.destino)

class transicion:
    def __init__ (self, origin, destiny, cost):
        self.origin = origin
        self.destiny = destiny
        self.cost = cost
    def __repr__ (self):
        return str (self.origin) + "--" + str(self.cost) + "--" + str(self.destiny)

def main (args):
    listaT = []
    alfabeto = ["a"]
    listaT.append (transicion (1, 2, "@"))
    listaT.append (transicion (2, 3, "a"))
    listaT.append (transicion(3, 4, "@"))

    #datos almacenados con éxito papá
    #for i in listaT:
     #   print (i.__repr__())
   
    resultado = calculo_subconjunto (listaT, alfabeto)
    #print (resultado[0].origen)

  #  print (resultado[0])

    for i in resultado:
        if(len (i.origen) > 0):
            print (i.origen,i.destino,i.costo)
    return 0

def existe (lista, elemento):
    bandera = 0
    for i in lista :
        if (i == elemento):
            bandera = 1
    return bandera

def mueve (T, a,listaT):

    temp = []
    salida = []
    for j in range (0, len(T)):
        for i in listaT:
            if (T[j] == i.origin):
                temp.append(i)

    for i in temp:
        if (a == i.cost):
            salida.append(i.destiny)
    return salida

def marcados (Estados):

    bandera = 1
    for i in Estados:
        if (i.marca == 0):
            bandera = 0
    return bandera

def pertenece (lista, estados):
    
    bandera = 0
    for i in estados:
        if ( i.lista == lista):
            bandera = 1
    return bandera

def calculo_cerradura( lista, listaT):

    #iniciar la pila y cerradura
    # cerradura es una lista vacía 
    pila = []
    cerradura = []
    for i in lista :
        pila.append (i)
        cerradura.append (i)


    while (len(pila) != 0):
        a = pila.pop()
        for i in listaT:
            if (i.origin == a):
                if (i.cost == '@'):
                    if (existe (cerradura, i.destiny) == 0):
                        pila.append(i.destiny)
                        cerradura.append(i.destiny)
    return cerradura

def calculo_subconjunto (listaT, alfabeto):

    a = []
    a.append (listaT[0].origin) 
    cerradura = []
    U = []
    cerradura = calculo_cerradura (a, listaT)
    Estados = []
    v = subconjunto (cerradura, 0)
    Estados.append (v)
    Estados[0].lista.sort()
    i = 0
    resultado = []

    while (marcados(Estados) != 1):
        Estados[i].marca = 1

        for j in alfabeto:
            temp = []
            temp2 = subconjunto([],0)
            temp = mueve (Estados[i].lista, j, listaT)
            U = calculo_cerradura (temp, listaT)
            U.sort()

            if (pertenece (U, Estados) == 0):
               # print ("entro")
                temp2 = subconjunto(U, 0)
                Estados.append(temp2)
                #print (temp2)
            aux = tranSub(Estados[i].lista, j, temp2)
            #print ("se inserta algo")
            resultado.append(aux)
            #print (aux.__repr__() )
        i = i+1
    return resultado

if __name__ == '__main__':
	import sys
	sys.exit (main(sys.argv))