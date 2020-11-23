import PySimpleGUI as sg
import os

sg.theme('DarkAmber')  # please make your creations colorful
lista = [['peque'],['peque'],['peque'],['peque']]
font = ('Courier New', 16)
text =  '\n'.join(lista[i][0] for i in range(len(lista)))
column = [[sg.Text(text, font=font)]]

layout = [
    [sg.Column(column, size=(800, 300), scrollable=True, key = "Column")],
    [sg.OK('ok', key='ok'), sg.Button('Up', key = "up"), sg.Button('Down', key = "down")],
]

window = sg.Window('Demo', layout, finalize=True)

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
#---------------------------------------------------#
if event == 'OK':
        MLINE_KEY = '-ML-'+sg.WRITE_ONLY_KEY 
        sg.Popup("Warning para leer esto :\n [ 'palabra' , linea ]")
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
        
#---------------------------------------------------------------------------------#
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
mlista = []
#----------------------------------------------------------------------------------------------------------#
#Sin comillas
for i in range(0,len(listan)):
    #lsita tamaño > 1
    palabra = lin(listan[i][1])
    if len(listan[i][1]) > 3:
        y = buscar(palabra[1][0],reservadas)
        x = buscar(palabra[1][0],relacionales)
        z = buscar(palabra[1][0],logicos)
        n = buscar(palabra[1][0],numerosB)
        k = buscar(palabra[1][0][0],errores)
        ll = buscar(palabra[1][0],arti)
        #----------------------------------#
        #buscar palabras reservadas
        if y == 1:
            mlista.append=(palabra)
            mlista.append=(palabra[1])
            lreservadas.append(mlista)
            del mlista[:]
        #buscar operaciones relacionales <= , >= , == , !=
        elif x == 1:
            mlista.append=(palabra)
            mlista.append=(palabra[1])
            loprelacional.append(mlista)
            del mlista[:]
        #buscar operaciones logicos && , ||
        elif z == 1:
            mlista.append=(palabra)
            mlista.append=(palabra[1])
            loplogico.append(mlista)
            del mlista[:]
        #buscar numeros de mas de dos digitos 1234
        elif n == 1:
            mlista.append=(palabra)
            mlista.append=(palabra[1])
            numeros.append(mlista)
            del mlista[:]
        #buscar errores
        elif k == 1:
            mlista.append=(palabra)
            mlista.append=(palabra[1])
            error.append(mlista)
            del mlista[:]
        #buscar ++ como artimetico
        elif ll == 1:
            mlista.append=(palabra)
            mlista.append=(palabra[1])
            lopAritmetico.append(mlista)
            del mlista[:]
        #Buscar identificador
        else:
            mlista.append=("ID")
            mlista.append=(palabra[1])
            lidentificador.append(mlista)
            del mlista[:]

        
    #lista tamaño == 1
    elif len(listan[i][1]) == 3:
        p = ord(palabra[1][0])
        #----------------------------------#
        #letras
        if p >= 65 and p <= 90 or p >= 97 and p <= 122:
            mlista.append=("ID")
            mlista.append=(palabra[1])
            lidentificador.append(palabra)
            del mlista[:]
        #----------------------------------#
        #parentesis
        elif p == 40 or p == 41:
            mlista.append=(palabra)
            mlista.append=(palabra[1])
            lparentesis.append(mlista)
            del mlista[:]
        #----------------------------------#
        #aritmeticos
        elif p == 42 or p == 43 or p == 45 or p == 47:
            mlista.append=(palabra)
            mlista.append=(palabra[1])
            lopAritmetico.append(palabra)
            del mlista[:]
        #----------------------------------#
        #Relacionales
        elif p >= 60 and p <= 62:
            mlista.append=(palabra)
            mlista.append=(palabra[1])
            loprelacional.append(palabra)
            del mlista[:]
        #corchetes
        elif p == 123 or p == 125:
            mlista.append=(palabra)
            mlista.append=(palabra[1])
            corchetes.append(palabra)
            del mlista[:]
        #Numeros un digito
        elif p >= 48 and p <= 57:
            mlista.append=("Nint")
            mlista.append=(palabra[1])
            numeros.append(palabra)
            del mlista[:]
        #brackets []
        elif p == 91 or p == 93:
            mlista.append=(palabra)
            mlista.append=(palabra[1])
            brackets.append(palabra)
            del mlista[:]

        #errores ['@','?','¡','¿','~']
        elif p == 64 or p== 63 or p == 141 or p == 168  or p == 126:
            error.append(palabra)

#----------------------------------------------------------------------------------------------------------#
#Con comillas

for i in range(0,len(listanSC)):
    palabra = lin(listanSC[i])

    if len(palabra[1]) > 5:
        mlista.append=("String")
        mlista.append=(palabra[1])
        lcadena.append(palabra)
        del mlista[:]
    
    elif len(palabra[1]) == 5:
        mlista.append=("Char")
        mlista.append=(palabra[1])
        lcaracter.append(palabra)
        del mlista[:]
if event == 'OK':
        MLINE_KEY = '-ML-'+sg.WRITE_ONLY_KEY
        print(lidentificador)
        print(lcadena)
        print(lcaracter)
        print(lopAritmetico)
        print(loprelacional)
        print(loplogico)
        print(lreservadas)
        print(lparentesis)
        print(numeros)
        print(corchetes)
        print(brackets)
        print(error)
        print(mlista)
