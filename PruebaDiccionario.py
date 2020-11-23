#!/usr/bin/env python
#-*-coding utf:-8-*-
import PySimpleGUI as sg
import os

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
    print(aux)
    #---------------------------------------------------------------------------------------------------#
    #Lmpieza
    cadenas = []
    aux2 = []
    aux3 = []
    for i in range(0,len(aux)):
        for j in range(0,len(aux[i])):
            if aux[i][j] == " ":
                print(aux3)
                aux4 = "".join(aux3)
                print(aux4)
                aux2.append(aux4)
                print(aux2)
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
        num=str(i+1)
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
    terminales.append("@")
    Ntermin = set(Nterminales)
    print(Ntermin)
    print(terminales)
    #---------------------------------------------------------------------------------------------------#
    #Impresion de diccionarios}
    file = open("EjemploF.txt","w")
    #UNO
    for key in dicc:
        file.write('Siguientes('+key+') = {'+(" ".join(dicc[key])+'}'+'\n'))

    file.write(os.linesep)

    #DOS
    for key in dicc:
        file.write('Primeros('+key+') = {'+(" ".join(dicc[key])+'}'+'\n'))

    


if __name__ == '__main__':
	main()