'''def impMatriz(matriz,filas,columnas):
    print("filas:",filas," columnas:",columnas)
    print("La matriz es la siguiente")
    for i in range(0,columnas):
        print("Una columna")
        for j in range(0,filas):
            print(matriz[j][i])
    
    impMatriz(matriz,filas,columnas)        #llamada de funcion

    imprimir matriz antes de que cada linea se convierta en string /////////////////////por si acaso 
'''
import os

Resultado = ["q2","q3","b","q1","q4","a"]
tamaño = len(Resultado)
filas = 3
columnas = int(float(tamaño/filas)) #generas el total de columnas a utilizar //
matriz = []
#-------------------------------------------------------------------------------------------------------------------------------#
#Creacion de matriz
for i in range(filas):
    matriz.append([])
    for j in range(columnas):
        matriz[i].append(None)

f = 0   #filas contador
c = 0   #columnas contador

#--------------------------------------------------------------------------------------------------------------------------------#
#llenado de matriz
for i in range(0,tamaño):
    if f == 3:
        f = 0
        c = c + 1
        matriz[f][c]=Resultado[i]
        f = f + 1

    else:
        matriz[f][c]= Resultado[i]
        f = f + 1

#---------------------------------------------------------------------------------------------------------------------------------#
#pasar columnas de matriz a string para guardar en archivo
#pasar a archivo los strings
file = open("C:/Users/KevinG/Desktop/5toSemestre/Compiladores/Python/Escribeme.txt","w")
aux = []
for i in range (0,columnas):
    for j in range (0,filas):
        aux.append(matriz[j][i])
    aux2 = " ".join(aux)    #convierte lista a string
    file.write("|"+aux2+"|"+os.linesep)
    del aux[:] 
file.close()
#-----------------------------------------------------------------------------------------------------------------------------------#

