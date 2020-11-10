import PySimpleGUI as sg
import os

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

lista = ""
contador = 0
for linea in f:
    if contador == 0:
        lista = lista + linea.strip('\n')
        contador = 1
    lista = lista + " " + linea.strip('\n')
             
f.close()
lista = lista + " "

print("lista=",lista[len(lista)-1])

file = open('lexico.txt','w')
f.write("Reservadas=",lreservadas)
f.write("identificadores=",lidentificador)
f.write("Aritmeticos=",lopAritmetico)
f.write("Relacionales=",loprelacional)
f.write("Parentesis=",lparentesis)
f.write("Corchetes",corchetes)
f.write("Numeros",numeros)
f.write("Brackets",brackets)
f.write("Errores",error)
f.write("Cadenas=",lcadena)
f.write("Caracteres=",lcaracter)
file.close()