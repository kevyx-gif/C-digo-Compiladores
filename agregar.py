import PySimpleGUI as sg
import os
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
Reglas2={}
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
ax = aux.copy()
ax.insert(0,letraAux+' -> '+letraAux+' $ ')
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
#Limpieza2
cadenas2 = []
aux6 = []
aux7= []
for k in range (0,len(ax)):
    for m in range (0,len(ax[k])):
        if ax[k][m] == " ":
            aux8 ="".join(aux7)
            aux6.append(aux8)
            del aux7[:]
        
        else:
            aux7.append(ax[k][m])
    aux9=aux6.copy()
    aux9.remove("->")
    cadenas2.append(aux9)
    del aux6[:]

print(cadenas)
print(cadenas2)
#---------------------------------------------------------------------------------------------------#
#Pasar a diccionarios  
#1
for i in range (0,len(cadenas)):
    num=str(i+1)
    cadena=" ".join(cadenas[i])
    valor=cadena.split(sep=" ")
    dicci=dict(zip([num],[valor]))
    Reglas.update(dicci)

for key in Reglas:
    print(key,":",Reglas[key])
print("Reglas 2")
#2
for j in range (0,len(cadenas2)):
    num2=str(j)
    cadena2=" ".join(cadenas2[j])
    valor2=cadena2.split(sep=" ")
    dicci2=dict(zip([num2],[valor2]))
    Reglas2.update(dicci2)


for key2 in Reglas2:
    print(key2,":",Reglas2[key2])

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
conjNT=[]
for m in range(0,len(Nterminales)):
    if((Nterminales[m] in conjNT)==False):
        conjNT.append(Nterminales[m])
Ntermin = sorted(set(Nterminales))
print(Ntermin)
print (terminales)
