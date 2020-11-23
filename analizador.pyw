#!/usr/bin/env python
#-*-coding utf: -8-*-
import PySimpleGUI as sg
import os

def lin(x):
    aux = []
    ulti = []
    for i in range (0,len(x)):
        if x[i] == "•":
            aux2 = " ".join(aux)
            ulti.append(aux2)
        
        elif i == len(x)-1:
            aux2 = " ".join(x[i])
            ulti.append(aux2)

        else:
            aux.append(x[i])
    return ulti


def buscar(x,y):
    bandera = 0
    for i in range(0,len(y)):
        if x.replace(" ", "") == y[i]:  #Replace quita los espacios en blanco
            bandera = 1
    return bandera
#Leer archivo
sg.theme('DarkAmber')  # please make your creations colorful

layout = [  [sg.Text('Nombre del archivo')],
            [sg.Input(), sg.FileBrowse()], 
            [sg.OK(), sg.Cancel()]
        ]


window = sg.Window('Toma de archivo', layout)
event, values = window.read()
print(values[0])
archivo = values[0]
window.close()
f = open(archivo)
        #poner nombre del archivo que se va a abrir
fila = 0
lista = ""
contador = 0
for linea in f:
    if contador == 0:
        lista = lista + linea.strip('\n') + " #"+str(fila)
        contador = 1
        fila = fila + 1 
    else:
        lista = lista + " " + linea.strip('\n')+" #"+str(fila)
        fila = fila + 1 
             
f.close()
lista = lista + " "
#Bibliotecas
reservadas = ['printf','int','float','char','scanf','main','return','for']
relacionales = ['==','<=','>=','!=']
logicos = ['&&','||']
numerosB = ['1','2','3','4','5','6','7','8','9','0']
errores = ['@','?','¡','¿','~']
arti = ['++','--']

cadena = "int main ( ) {          int a , b , c = 1 , 2 , 3 ;            float d = 4 ;   char x = \"h\" ;      printf ( \"%d%d%d\\n\" , a , b , c ) ; "
cadena2 = lista
aux = []
aux2 = []
lista = []
listEr = []
i = 0
cfila = 0
mini_lista = []
print (cadena2)
#----------------------------------------------------------------------------------------------------------#
#Separar Strings,char de todo lo demas
while (i < len(cadena2) ):
    
    #Acumular letras por si son mas de 1 y guardarlas en un aux
    if cadena2[i] != " " and cadena2[i] != "\"" and cadena2[i] != "#":
        aux.append(cadena2[i])

    #Si se detecta que tiene comillas al inicio se ira como String o caracter
    elif cadena2[i] == "\"":
        j = i
        while (cadena2[j] != " "):
            aux.append(cadena2[j])
            j = j + 1
        aux2 = "".join(aux)
        if len(aux2) > 1 :
            mini_lista.append(str(cfila))
            mini_lista.append("String")
            mini_lista.append(aux2)
            mlist = mini_lista.copy()
            lista.append(mlist)
            del mini_lista[:]
            del aux[:]
        
        elif len(aux2) == 1 :
            mini_lista.append(str(cfila))
            mini_lista.append("char")
            mini_lista.append(aux2)
            mlist = mini_lista.copy()
            lista.append(mlist)
            del mini_lista[:]
            del aux[:]

        i = j
      
    #Si llega a un espacio , lo que tiene aux se agrega a la lista de 1 a mas caracteres en aux
    elif cadena2[i] == " ":
        aux2 = "".join(aux)
        #Si la palabra es mayor a 1
        if len(aux2) > 1 :
            x = buscar(aux2,reservadas)
            y = buscar(aux2,relacionales)
            z = buscar(aux2,logicos)
            n = buscar(aux2,numerosB)
            k = buscar(aux2,errores)
            ll = buscar(aux2,arti)
            

            #----------------------------------#
            #buscar palabras reservadas
            if x == 1:
                mini_lista.append(str(cfila))
                mini_lista.append(aux2)
                mini_lista.append(aux2)
                mlist = mini_lista.copy()
                lista.append(mlist)

                del mini_lista[:]
                del aux[:]
            #buscar operaciones relacionales <= , >= , == , !=
            elif y == 1:
                mini_lista.append(str(cfila))
                mini_lista.append(aux2)
                mini_lista.append(aux2)
                mlist = mini_lista.copy()
                lista.append(mlist)

                del mini_lista[:]
                del aux[:]
            #buscar operaciones logicos && , ||
            elif z == 1:
                mini_lista.append(str(cfila))
                mini_lista.append(aux2)
                mini_lista.append(aux2)
                mlist = mini_lista.copy()
                lista.append(mlist)

                del mini_lista[:]
                del aux[:]
                
            #buscar numeros de mas de dos digitos 1234
            elif n == 1:
                mini_lista.append(str(cfila))
                mini_lista.append("Nint")
                mini_lista.append(aux2)
                mlist = mini_lista.copy()
                lista.append(mlist)

                del mini_lista[:]
                del aux[:]
            #buscar errores
            elif k == 1:
                mini_lista.append(str(cfila))
                mini_lista.append(aux2)
                mini_lista.append(aux2)
                mlist = mini_lista.copy()
                listEr.append(mlist)

                del mini_lista[:]
                del aux[:]
            #buscar ++ como artimetico
            elif ll == 1:
                mini_lista.append(str(cfila))
                mini_lista.append(aux2)
                mini_lista.append(aux2)
                mlist = mini_lista.copy()
                lista.append(mlist)

                del mini_lista[:]
                del aux[:]
            #Buscar identificador
            else:
                mini_lista.append(str(cfila))
                mini_lista.append("ID")
                mini_lista.append(aux2)
                mlist = mini_lista.copy()
                lista.append(mlist)

                del mini_lista[:]
                del aux[:]
        #Palabra  igual 1 
        elif len(aux2) == 1:
            p = ord(aux2)
            #----------------------------------#
            #letras
            if p >= 65 and p <= 90 or p >= 97 and p <= 122:
                mini_lista.append(str(cfila))
                mini_lista.append("ID")
                mini_lista.append(aux2)
                mlist = mini_lista.copy()
                lista.append(mlist)

                del mini_lista[:]
                del aux[:]
            #----------------------------------#
            #parentesis
            elif p == 40 or p == 41:
                mini_lista.append(str(cfila))
                mini_lista.append(aux2)
                mini_lista.append(aux2)
                mlist = mini_lista.copy()
                lista.append(mlist)

                del mini_lista[:]
                del aux[:]
            #----------------------------------#
            #aritmeticos
            elif p == 42 or p == 43 or p == 45 or p == 47:
                mini_lista.append(str(cfila))
                mini_lista.append(aux2)
                mini_lista.append(aux2)
                mlist = mini_lista.copy()
                lista.append(mlist)

                del mini_lista[:]
                del aux[:]
            #----------------------------------#
            #Relacionales
            elif p >= 60 and p <= 62:
                mini_lista.append(str(cfila))
                mini_lista.append(aux2)
                mini_lista.append(aux2)
                mlist = mini_lista.copy()
                lista.append(mlist)

                del mini_lista[:]
                del aux[:]
            #corchetes
            elif p == 123 or p == 125:
                mini_lista.append(str(cfila))
                mini_lista.append(aux2)
                mini_lista.append(aux2)
                mlist = mini_lista.copy()
                lista.append(mlist)
                del mini_lista[:]
                del aux[:]
            #Numeros un digito
            elif p >= 48 and p <= 57:
                mini_lista.append(str(cfila))
                mini_lista.append("Nint")
                mini_lista.append(aux2)
                mlist = mini_lista.copy()
                lista.append(mlist)
                del mini_lista[:]
                del aux[:]
            #brackets []
            elif p == 91 or p == 93:
                mini_lista.append(str(cfila))
                mini_lista.append(aux2)
                mini_lista.append(aux2)
                mlist = mini_lista.copy()
                lista.append(mlist)
                del mini_lista[:]
                del aux[:]

            #errores ['@','?','¡','¿','~']
            elif p == 64 or p== 63 or p == 141 or p == 168  or p == 126:
                mini_lista.append(str(cfila))
                mini_lista.append(aux2)
                mini_lista.append(aux2)
                mlist = mini_lista.copy()
                listEr.append(mlist)
                del mini_lista[:]
                del aux[:]


    elif cadena2[i] == "#":
        cfila = cfila + 1
        i = i + 2

    i = i +1 
axu4 = ['linea','token','lexema']
lista.insert(0,axu4)
aux4 = ['Tabla de errores']
lista.append(aux4)
lista.append(listEr)
for i in range(0,len(lista)):
    print(lista[i])
#----------------------------------------------------------------------------------------------------------#
#Tener listas para ir separando de acuerdo a lo que son
aux3 = []
cont = 0

if event == 'OK':
    font = ('Courier New', 16)
    for i in range(0, len(lista)) :
        text = '\n'.join(map(str,lista))
    column = [[sg.Text(text, font=font)]]
    layout = [
        [sg.Column(column, size=(800, 300), scrollable=True, key = "Column")],
        [sg.OK('ok', key='ok'), sg.Button('Up', key = "up"), sg.Button('Down', key = "down")],
    ]

    window = sg.Window('Analizador Lexico', layout, finalize=True)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == "down":
            window['Column'].Widget.canvas.yview_moveto(1.0)
        elif event == "up":
            window['Column'].Widget.canvas.yview_moveto(0.0)

        elif event == "ok":
            break
    
    window.close()
            

#cambiar errores por identificadores ,para que si no tiene las letras /aA,bB o cualquier otro , se vaya como error , agregar (;) para reconocerlo