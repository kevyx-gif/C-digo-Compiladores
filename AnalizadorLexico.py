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
reservadas = ['printf','int','float','char','scanf','main','return']
relacionales = ['==','<=','>=','!=']
logicos = ['&&','||']
numerosB = ['1','2','3','4','5','6','7','8','9','0']
errores = ['@','?','¡','¿','~']

cadena = "int main ( ) {          int a , b , c = 1 , 2 , 3 ;            float d = 4 ;   char x = \"h\" ;      printf ( \"%d%d%d\\n\" , a , b , c ) ; "
cadena2 = lista
aux = []
lista = []
listaSC = []
i = 0
cfila = 0
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
        listaSC.append(aux2+"•"+str(cfila))
        del aux[:]
        i = j
      
    #Si llega a un espacio , lo que tiene aux se agrega a la lista de 1 a mas caracteres en aux
    elif cadena2[i] == " ":
        if aux[0] != "#":
            aux2 = "".join(aux)
            lista.append(aux2+"•"+str(cfila))
        del aux[:]

    elif cadena2[i] == "#":
        aux.append(cadena2[i])
        cfila = cfila + 1

    i = i +1 

#----------------------------------------------------------------------------------------------------------#
#Tener listas para ir separando de acuerdo a lo que son

listan = lista      
listanSC = listaSC         

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
error = []
#----------------------------------------------------------------------------------------------------------#
#Sin comillas
for i in range(0,len(listan)):
    #lsita tamaño > 1
    palabra = lin(listan[i])
    if len(listan[i]) > 3:
        y = buscar(palabra[0],reservadas)
        x = buscar(palabra[0],relacionales)
        z = buscar(palabra[0],logicos)
        n = buscar(palabra[0],numerosB)
        k = buscar(palabra[0][0],errores)
        #----------------------------------#
        #buscar palabras reservadas
        if y == 1:
            lreservadas.append(palabra)
        #buscar operaciones relacionales <= , >= , == , !=
        elif x == 1:
            loprelacional.append(palabra)
        #buscar operaciones logicos && , ||
        elif z == 1:
            loplogico.append(palabra)
        #buscar numeros de mas de dos digitos 1234
        elif n == 1:
            numeros.append(palabra)

        elif k == 1:
            error.append(palabra)

        else:
            lidentificador.append(palabra)

        
    #lista tamaño == 1
    elif len(listan[i]) == 3:
        p = ord(palabra[0])
        #----------------------------------#
        #letras
        if p >= 65 and p <= 90 or p >= 97 and p <= 122:
            lidentificador.append(palabra)
        #----------------------------------#
        #parentesis
        elif p == 40 or p == 41:
            lparentesis.append(palabra)
        #----------------------------------#
        #aritmeticos
        elif p == 42 or p == 43 or p == 45 or p == 47:
            lopAritmetico.append(palabra)
        #----------------------------------#
        #Relacionales
        elif p >= 60 and p <= 62:
            loprelacional.append(palabra)
        #corchetes
        elif p == 123 or p == 125:
            corchetes.append(palabra)
        #Numeros un digito
        elif p >= 48 and p <= 57:
            numeros.append(palabra)
        #brackets []
        elif p == 91 or p == 93:
            brackets.append(palabra)

        #errores ['@','?','¡','¿','~']
        elif p == 64 or p== 63 or p == 141 or p == 168  or p == 126:
            error.append(palabra)

#----------------------------------------------------------------------------------------------------------#
#Con comillas

for i in range(0,len(listanSC)):
    palabra = lin(listanSC[i])

    if len(palabra[0]) > 5:
        lcadena.append(palabra)
    
    elif len(palabra[0]) == 5:
        lcaracter.append(palabra)

if event == 'OK':
        MLINE_KEY = '-ML-'+sg.WRITE_ONLY_KEY 
        sg.Popup("Reservadas=",lreservadas)
        sg.Popup("identificadores=",lidentificador)
        sg.Popup("Aritmeticos=",lopAritmetico)
        sg.Popup("Relacionales=",loprelacional)
        sg.Popup("Parentesis=",lparentesis)
        sg.Popup("Corchetes",corchetes)
        sg.Popup("Numeros",numeros)
        sg.Popup("Brackets",brackets)
        sg.Popup("Errores",error)
        sg.Popup("Cadenas=",lcadena)
        sg.Popup("Caracteres=",lcaracter)
        layoutt= [[sg.Multiline("Terminado", size=(20,2), key=MLINE_KEY)],
            [sg.Button('OK')]]
        windows = sg.Window('resultados',layoutt)  
        while True:             # Event Loop
            evento, values = windows.read()
            if evento in (sg.WIN_CLOSED, 'OK'):
                break
        windows.close()
