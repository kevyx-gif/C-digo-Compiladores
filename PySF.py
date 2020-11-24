#!/usr/bin/env python
#-*-coding utf:-8-*-
import PySimpleGUI as sg
import os

class estados:
    def __init__ (self, origen, derivada):
        self.origen = origen
        self.derivada = derivada

class NoTerminales:
    def __init__ (self, origen, primeros):
        self.origen =  origen
        self.primeros =  primeros

def main():
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
    Reglas={}
    aux=[]
    cont = 0
    f = open(archivo)
    for linea in f:
        if cont == 0:
            cont = cont + 1
        else:
            linea = linea.replace('\n',' ')
            aux.append(linea)
    #print(aux)
    #---------------------------------------------------------------------------------------------------#
    #Lmpieza
    cadenas = []
    aux2 = []
    aux3 = []
    for i in range(0,len(aux)):
        for j in range(0,len(aux[i])):
            if aux[i][j] == " ":
                #print(aux3)
                aux4 = "".join(aux3)
                #print(aux4)
                aux2.append(aux4)
                #print(aux2)
                del aux3[:]
            
            else:
                aux3.append(aux[i][j])
        aux5=aux2.copy()
        aux5.remove("->")
 
        cadenas.append(aux5)
        del aux2[:]
    #---------------------------------------------------------------------------------------------------#
    #Pasar a diccionarios  
    #print (cadenas)
    for i in range (0,len(cadenas)):
        num=str(i+1)
        cadena=" ".join(cadenas[i])
        valor=cadena.split(sep=" ")
        dicci=dict(zip([num],[valor]))
        Reglas.update(dicci)

    #for key in Reglas:
    #    print(key,":",Reglas[key])

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
    terminales.append("@")
    conjNT=[]
    for m in range(0,len(Nterminales)):
        if((Nterminales[m] in conjNT)==False):
            conjNT.append(Nterminales[m])
    Ntermin = set(Nterminales)

    #print (conjNT)
    #print (Ntermin)
    #print (terminales)
    Prim=[]
    Prim=trabajar(Reglas,conjNT) #Se llama a Primeros
    i=0
    while i < len(Prim):
        a = Prim[i+1][0]
        b = "".join(Prim[i])
        print("Primeros ("+b+") = ",a)
        i = i + 2
    Sigu={}
    Sigu=Siguientes(conjNT,Reglas) #Se llama a Siguientes
    for key in Sigu:
        #print(key,":",Sig[key])
        print('Siguientes('+key+') = ',Sigu[key]) 
    
    #---------------------------------------------------------------------------------------------------#
    #Impresion de diccionarios
    file = open("EjemploF.txt","w")
    #UNO
    i = 0
    while i < len(Prim):
        a = " ".join(Prim[i+1][0])
        b = "".join(Prim[i])
        file.write("Primeros ("+b+") = { "+a+' }'+'\n')
        i = i + 2

    file.write(os.linesep)

    #DOS
    for key in Sigu:
        file.write('Siguientes('+key+') = { '+(" ".join(Sigu[key])+' }'+'\n'))

    sg.popup("Resultado guardado en EjemploF")

#------------------------Metodo Siguientes---------------------------------------------------

def Siguientes(conjNT,Reglas): #Siguientes(X)
    Sig={}
    for i in range (0,len(conjNT)): #Se inicializa el diccionario de Siguientes
        temp2=[]
        temp=dict(zip([conjNT[i]],[temp2]))
        Sig.update(temp)

    for i in range(0,len(conjNT)): #Inician las reglas
        if (i==0): #Inicio Regla 1
            #print("Se cumple regla 1")
            temp2=['$']
            temp=dict(zip([conjNT[i]],[temp2]))
            Sig.update(temp)
        else:
            for key in Reglas:
                if(conjNT[i]==Reglas[key][1] and len(Reglas[key])==2):
                    temp2=['$']
                    temp=dict(zip([conjNT[i]],[temp2]))
                    Sig.update(temp)   #Fin Regla 1

        for key in Reglas: #Inicio Regla 2
            for j in range(1,len(Reglas[key])):
                if (conjNT[i]==Reglas[key][j]):
                    #print("Se encontró",conjNT[i],"en",key,"posicion:",j)
                    if (len(Reglas[key])>2 and j<=len(Reglas[key])-2):
                        #print("Se cumple la regla 2")
                        #temp=Primeros(Reglas[key][j+1])  --Esta sera la regla una vez implemente Mike Primeros
                        temp2=Reglas[key][j+1]
                        Sig[conjNT[i]].append(temp2)#Fin Regla 2
                    elif(len(Reglas[key])>2 and j==len(Reglas[key])-1 and conjNT[i]!=Reglas[key][0]): #Inicio Regla 3
                        #print("Se cumple la regla 3")
                        temp2=Sig[Reglas[key][0]]
                        for n in range(0,len(temp2)):
                            #print('entra')
                            if ((temp2[n] in Sig[conjNT[i]]) == False):
                                #print('Entra2')
                                temp=temp2[n]
                                Sig[conjNT[i]].append(temp)
    return Sig

#-------------------------------------------Metodo Primeros-----------------------------------------------

def posicion (x, listaEstados):
    #regresa la posicion donde están las reglas de derivacion
    for i in range (0, len(listaEstados)):
        if (listaEstados[i].origen == x):
            return i

def copiar_derivadas (indice, listaEstados):
    lista = []
    for i in listaEstados[indice].derivada:
        lista.append (i)
    return lista

def primeros (listaEstados, listaNT, Lresultados):
    indice = 0
    while (indice < len(listaNT)):
        Lprimeros = []
        letra = listaNT[indice]
        aux = calcular_primeros(letra, listaEstados, listaNT)
        #aux = [0]
        Lprimeros.append (aux)
        aux2 = NoTerminales (letra, Lprimeros)
        Lresultados.append (aux2)
        indice = indice + 1

def no_terminal (letra, lista):
    bandera = 0
    for i in lista:
        if(i == letra):
            bandera = 1

    return bandera

def calcular_primeros (x, listaEstados, listaNT):
    ent = []
    indice = posicion(x, listaEstados)

    while (indice < len(listaEstados) and listaEstados[indice].origen == x):
        lista = copiar_derivadas (indice, listaEstados)

        for i in range (0, len (lista)):
            if (lista[i] in listaNT):
               # print(x, lista[i])
                if (lista[i] ==  x):
                    break
                else:
                    ent = calcular_primeros (lista[i], listaEstados, listaNT)
                    break
            else:
                ent.append(lista[i])
                break
        indice = indice +1
    return ent

def convertir_a_estados (lista, diccionario):

    for i in diccionario:
        laux = diccionario[i]
        origen = laux[0]
        derivada = []
        for j in range (1, len(laux)):
            derivada.append(laux[j])
        aux = estados (origen, derivada)
        lista.append(aux)


def trabajar (Reglas, listaNT):
    Lresultados = []
    listaEstados = []
    reg=[]
    convertir_a_estados (listaEstados, Reglas)
    primeros(listaEstados, listaNT, Lresultados)

    for i in Lresultados:
        reg.append(i.origen)
        reg.append(i.primeros)
    
    return reg

if __name__ == '__main__':
	main()