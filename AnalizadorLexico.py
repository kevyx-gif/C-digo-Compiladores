import PySimpleGUI as sg
import os

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

lista = ""
contador = 0
for linea in f:
    if contador == 0:
        lista = lista + linea.strip('\n')
        contador = 1
    lista = lista + " " + linea.strip('\n')
             
f.close()
lista = lista + " "
#Bibliotecas
reservadas = ['printf','int','float','char','scanf','main','return']
relacionales = ['==','<=','>=','!=']
logicos = ['&&','||']
numerosB = ['1','2','3','4','5','6','7','8','9','0']

cadena = "int main ( ) {          int a , b , c = 1 , 2 , 3 ;            float d = 4 ;   char x = \"h\" ;      printf ( \"%d%d%d\\n\" , a , b , c ) ; "
cadena2 = lista
aux = []
lista = []
listaSC = []
i = 0

#----------------------------------------------------------------------------------------------------------#
#Separar Strings,char de todo lo demas
while (i < len(cadena2) ):
    
    #Acumular letras por si son mas de 1 y guardarlas en un aux
    if cadena2[i] != " " and cadena2[i] != "\"":
        aux.append(cadena2[i])

    #Si se detecta que tiene comillas al inicio se ira como String o caracter
    elif cadena2[i] == "\"":
        j = i
        while (cadena2[j] != " "):
            aux.append(cadena2[j])
            j = j + 1

        aux2 = " ".join(aux)
        listaSC.append(aux2)
        del aux[:]
        i = j
      
    #Si llega a un espacio , lo que tiene aux se agrega a la lista de 1 a mas caracteres en aux
    elif cadena2[i] == " ":
        aux2 = " ".join(aux)
        lista.append(aux2)
        del aux[:]

    i = i +1 

#----------------------------------------------------------------------------------------------------------#
#Tener listas para ir separando de acuerdo a lo que son

listan = list(set(lista)) #Quitar objetos repetidos de la lista
listanSC = list(set(listaSC))  #Quitar objetos repetidos de la listaSC
print("Sin comillas",listan)
print("Con comillas",listaSC)

lidentificador = []
lcadena = []
lcaracter = []
lopAritmetico = []
loprelacional = []
loplogico = []
lreservadas = []
lparentesis = []
numeros = []
corchetes = []
brackets = []
#----------------------------------------------------------------------------------------------------------#
#Sin comillas
for i in range(0,len(listan)):
    #lsita tamaño > 1
    if len(listan[i]) > 1:
        y = buscar(listan[i],reservadas)
        x = buscar(listan[i],relacionales)
        z = buscar(listan[i],logicos)
        n = buscar(listan[i],numerosB)
        #----------------------------------#
        #buscar palabras reservadas
        if y == 1:
            lreservadas.append(listan[i])
        #buscar operaciones relacionales <= , >= , == , !=
        elif x == 1:
            loprelacional.append(listan[i])
        #buscar operaciones logicos && , ||
        elif z == 1:
            loplogico.append(listan[i])
        #buscar numeros de mas de dos digitos 1234
        elif n == 1:
            numeros.append(listan[i])

        else:
            lidentificador.append(listan[i])

        
    #lista tamaño == 1
    elif len(listan[i]) == 1:
        p = ord(listan[i])
        #----------------------------------#
        #letras
        if p >= 65 and p <= 90 or p >= 97 and p <= 122:
            lidentificador.append(listan[i])
        #----------------------------------#
        #parentesis
        elif p == 40 or p == 41:
            lparentesis.append(listan[i])
        #----------------------------------#
        #aritmeticos
        elif p == 42 or p == 43 or p == 45 or p == 47:
            lopAritmetico.append(listan[i])
        #----------------------------------#
        #Relacionales
        elif p >= 60 and p <= 62:
            loprelacional.append(listan[i])
        #corchetes
        elif p == 123 or p == 125:
            corchetes.append(listan[i])
        #Numeros un digito
        elif p >= 48 and p <= 57:
            numeros.append(listan[i])
        #brackets []
        elif p == 91 or p == 93:
            brackets.append(listan[i])

#Impresiones
print("Reservadas=",lreservadas)
print("identificadores=",lidentificador)
print("Aritmeticos=",lopAritmetico)
print("Relacionales=",loprelacional)
print("Parentesis=",lparentesis)
print("Corchetes",corchetes)
print("Numeros",numeros)
print("Brackets",brackets)
#----------------------------------------------------------------------------------------------------------#
#Con comillas

for i in range(0,len(listanSC)):
    p = listanSC[i].replace(" ", "")

    if len(p) > 3:
        lcadena.append(p)
    
    elif len(p) == 3:
        lcaracter.append(p)

print("Cadenas=",lcadena)
print("Caracteres=",lcaracter)