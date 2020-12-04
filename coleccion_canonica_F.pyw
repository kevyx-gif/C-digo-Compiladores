#!/usr/bin/env python
#-*-coding utf:-8-*-

class gramatica :
    def __init__ (self, origen, derivada):
        self.origen = origen
        self.derivada = derivada
    def __repr__ (self):
        return str (self.origen) + "-> " + str (self.derivada)

class estados :
    def __init__ (self, numero, conjuntoC):
        self.numero = numero
        self.conjuntoC = conjuntoC
    def __repr__ (self):
        return str (self.numero) + " := " + str (self.conjuntoC)

def convertir_a_estados (lista, diccionario):

    for i in diccionario:
        laux = diccionario[i]
        origen = laux[0]
        derivada = []
        for j in range (1, len(laux)):
            derivada.append(laux[j])
        aux = gramatica (origen, derivada)
        lista.append(aux)

def indice_punto (listaDerivada):
    #regresa la posicion siguiente de donde se encuentra el punto
    for i in range (0, len(listaDerivada)):
        if (listaDerivada[i] == '•'):
            return i+1

def indice_gramatica (LGramatica, X ):
    #regresa la posicion de donde se encuentre la regla gramatical buscara
    for i in range (0, len(LGramatica)):
        if (X == LGramatica[i].origen):
            return i

def poner_punto (derivadas):
    #colocar el punto en una derivada de gramatica nueva
    temp = derivadas.copy()
    temp2 = ['•']
    for i in temp:
        temp2.append (i)

    return temp2

def pertenece_conjunto (a, listaA):
    bandera = 0
    for i in listaA:
        if (i.origen == a.origen):
            if (len(i.derivada) == len(a.derivada)):
                j = 0
                while ( j <  len (i.derivada)):
                    if (i.derivada[j] != a.derivada[j]):
                        break
                    j = j+1
                if (j == len (a.derivada)):
                    bandera = 1
    return bandera 

def pertenece_conjuntoC (conjunto, ListaEstados):
    bandera = 0
    for i in ListaEstados:
        #print (conjunto)
        #print ( i.conjuntoC)
        if (len (i.conjuntoC) == len (conjunto)):
            h = 0
            for j in range (0, len(i.conjuntoC)):
                if (conjunto[h].origen == i.conjuntoC[j].origen):
                    
                    if (len (conjunto[h].derivada) == len (i.conjuntoC[j].derivada)):
                        #print ("lee este de aca " ,conjunto[0])
                        #print (conjunto[j] , "   " , i.conjuntoC[j] )
                        k = 0
                        while (k < len (conjunto[h].derivada) and h < len (i.conjuntoC) ):
                            if (i.conjuntoC[h].derivada[k] != conjunto[h].derivada[k]):
                                break
                            k = k+1
                        if (k == len (conjunto[h].derivada)):
                            bandera = 1
                            #print ("aca hay cambio")
            h = h+1
    #print (bandera, "\n")
    return bandera

def indice_coincidencia (conjunto, Lconjunto):
    indice = -1
    for i in range (0, len (Lconjunto)):
        #print (conjunto)
        #print ( i.conjuntoC)
        if (len (Lconjunto[i].conjuntoC) == len (conjunto)):
            h = 0
            for j in range (0, len(Lconjunto[i].conjuntoC)):
                if (conjunto[h].origen == Lconjunto[i].conjuntoC[j].origen):
                    
                    if (len (conjunto[h].derivada) == len (Lconjunto[i].conjuntoC[j].derivada)):
                        #print ("lee este de aca " ,conjunto[0])
                        #print (conjunto[j] , "   " , i.conjuntoC[j] )
                        k = 0
                        while (k < len (conjunto[h].derivada)):
                            if (Lconjunto[i].conjuntoC[h].derivada[k] != conjunto[h].derivada[k]):
                                break
                            k = k+1
                        if (k == len (conjunto[h].derivada)):
                            indice = i
                            #print ("aca hay cambio")
            h = h+1
    #print (bandera, "\n")
    return indice

def cerradura (Cgramatica, listaNT, LGramatica):
    
    #print ("cerradura")
    for i in Cgramatica:
        #sacar indice donde se encuentra el punto
        aux = indice_punto (i.derivada)  

        if ( aux < len(i.derivada) and i.derivada[aux] in listaNT):
            #sacar indice donde esté la regla de producción no terminal B
            indice = indice_gramatica (LGramatica, i.derivada[aux])

            while ( indice < len(LGramatica) and LGramatica[indice].origen == i.derivada[aux]):
                temp = poner_punto (LGramatica[indice].derivada)
                objetoT = gramatica (LGramatica[indice].origen, temp)

                if (pertenece_conjunto (objetoT, Cgramatica) == 0):
                    Cgramatica.append(objetoT)

                indice = indice +1
    
    return Cgramatica
                
def despuesPunto (lista, x):
    indice = indice_punto (lista.derivada)
    if (indice < len (lista.derivada ) and lista.derivada[indice] == x):
        return 1
    return 0


def actualizar_punto (G):

    temp = []
    i = 0
    while (i < len (G.derivada)):
        if (G.derivada[i] == '•' and i < (len (G.derivada) - 1)):
            temp.append(G.derivada[i+1])
            temp.append (G.derivada[i])
            i = i +1
        else:
            temp.append (G.derivada[i])
        i = i +1
        
    aux = gramatica (G.origen, temp)
    return aux


def Ir_a (I, listaNT, LGramatica, x):
    J = []
    for i in I.conjuntoC:
        if (despuesPunto (i, x) == 1):
            temp = actualizar_punto(i)
            J.append (temp)
    return cerradura(J, listaNT, LGramatica)

def simbolo_gramatical (derivadas):
    indice = indice_punto (derivadas)
    if (indice == len(derivadas)):
        return None

    return derivadas[indice]


def conjunto_vacio (conjunto):
    #regresa un uno si es un conjunto vacio
    #regresa un cero en caso contrario
    if (len(conjunto) > 0):
        return 0
    return 1


def coleccion_canonica (listaNT, LGramatica):
    file = open("EjemploF.txt","w")
    C = []
    temp = gramatica (LGramatica[0].origen, LGramatica[0].derivada.copy() )
    temp.derivada = poner_punto (temp.derivada)
    Ltemp = [temp]
    aux = cerradura (Ltemp, listaNT, LGramatica)
    nuevo = estados(0, aux)
    m2 = str(nuevo.numero)
    m4 = []
    for txs in nuevo.conjuntoC:
        m4.append(txs.origen)
        m4.append("-> [")
        m3 = "  ".join(txs.derivada)
        m4.append(m3+"]")
    m5 = " ".join(m4)

    file.write("I0 :=  "+m5+" \n"+"\n")
    C.append (nuevo)

    for i in C:
        anterior = ''
        for j in i.conjuntoC:
            x = simbolo_gramatical (j.derivada)

            if (x != None and x!= anterior):
                if (x != '@'):
                    print ("\nIr_a(", i.numero, "," , x , ")")
                    num = str(i.numero)
                    num2 = str(x)
                    file.write("Ir_a( \'"+num+"\' , \'"+num2+"\' )\n")
                if (x == '$'):
                    print ("aceptacion")
                    file.write("aceptacion\n")
                elif(x!='@'):
                    nuevoConjunto = Ir_a(i, listaNT, LGramatica, x)
                    if (conjunto_vacio(nuevoConjunto) == 0 and pertenece_conjuntoC (nuevoConjunto, C) == 0):
                        nuevoEstado = estados (len (C), nuevoConjunto)
                        C.append (nuevoEstado)
                        print (nuevoEstado)
                        num3 = str(nuevoEstado.numero)
                        ax = []
                        for mn in nuevoEstado.conjuntoC:
                            ax.append(mn.origen)
                            ax.append("-> [")
                            qe = "  ".join(mn.derivada)
                            ax.append(qe+"]")
                        ax2 = " ".join(ax)
                        file.write(num3+":= "+ax2+"\n")
                        del ax[:]
                        


                    elif (conjunto_vacio(nuevoConjunto) == 0):
                        a = indice_coincidencia (nuevoConjunto, C)
                        print (":= ",a)
                        num7 = str(a)
                        file.write(":= "+num7+"\n")

            anterior = x
    return C

def main ():
    #---------------------------------------------------------------------------------------------------#
    sg.theme('DarkAmber')  # please make your creations colorful

    layout = [  [sg.Text('Nombre del archivo')],
                [sg.Input(), sg.FileBrowse()], 
                [sg.OK(), sg.Cancel()]
            ]
    window = sg.Window('Toma de archivo', layout)
    event,values = window.read()
    if event == 'OK':
        archivo = values[0]
    window.close()
    #---------------------------------------------------------------------------------------------------#
    dicc={}
    aux=[]
    cont = 0
    f = open(archivo)
    for linea in f:
        if cont == 0:
            cont = cont + 1
        else:
            linea = linea.replace('\n',' ')
            aux.append(linea)
    letraAux = aux[0][0]
    aux.insert(0,letraAux+' -> '+letraAux+' $ ')
    print(aux)
    #---------------------------------------------------------------------------------------------------#
    #Lmpieza
    cadenas = []
    aux2 = []
    aux3 = []
    for i in range(0,len(aux)):
        for j in range(0,len(aux[i])):
            if aux[i][j] == " ":
                aux4 = "".join(aux3)
                aux2.append(aux4)
                del aux3[:]
            
            else:
                aux3.append(aux[i][j])
        aux5=aux2.copy()
        aux5.remove("->")
 
        cadenas.append(aux5)
        del aux2[:]
    #---------------------------------------------------------------------------------------------------#
    #Pasar a diccionarios  
    print (cadenas)
    for i in range (0,len(cadenas)):
        num=str(i)
        cadena=" ".join(cadenas[i])
        valor=cadena.split(sep=" ")
        dicci=dict(zip([num],[valor]))
        dicc.update(dicci)

    for key in dicc:
        print(key,":",dicc[key])

    #---------------------------------------------------------------------------------------------------#
    #pasar a terminales y no terminales
    terminales = []
    Nterminales = []
    for i in range(0,len(cadenas)):
        bandera = 0
        for j in  range(0,len(cadenas[i])):
            if bandera == 0:
                Nterminales.append(cadenas[i][j])
                bandera = bandera + 1
            else:
                if len(cadenas[i][j]) > 1:
                    terminales.append(cadenas[i][j])
                elif len(cadenas[i][j]) == 1:
                    p = ord(cadenas[i][j])
                    if p < 65 or p > 90:
                        terminales.append(cadenas[i][j])
    Ntermin = set(Nterminales)
    print(Ntermin)
    print(terminales)
    #--------------------#
    LGramatica = []
    convertir_a_estados (LGramatica, dicc)
    C = coleccion_canonica (Ntermin, LGramatica)
    


if __name__ == '__main__':
    import PySimpleGUI as sg
    import os
    main ()