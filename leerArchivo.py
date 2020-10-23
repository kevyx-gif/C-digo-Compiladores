alfabeto = "alfabeto"
expresion = "expresion"
contador = 0
f = open("prueba.txt")
        #poner nombre del archivo que se va a abrir
        
for linea in f:
    if contador == 0:
        alfabeto = linea[:-1]   #Sirve para quitar el salto de linea y que no se lea en las cadenas
        contador = contador + 1

    else:
        expresion = linea           
f.close()

#Usar como separador "," no pones espacios y "." para terminar  Solo para el diccionario  ||  Alfabeto = a,b,c,letra,digito.
#----------------------------------------------------------------------------------------------------------------------------------------------------#
#Separacion de palabras para agregar a la caja(diccionario)
#checar a partir de el indice 11 (es donde inicia el diccionario)
print(alfabeto)

caja=[]
aux = []
for i in range (11,len(alfabeto)):
    if alfabeto[i] != "," and alfabeto[i] != ".":
        aux.append(alfabeto[i]) #agregar al auxiliar letra para formar la palabra
    
    else:
        aux2 = " ".join(aux)        #convierte a String la lista
        caja.append(aux2)       #agregar al diccionario la palabra
        del aux[:]      #reinicio de auxiliar 
print(caja)
#-----------------------------------------------------------------------------------------------------------------------------------------------------#
#Guardar la expresion en una sola lista
#Checar a partir del indice  12 (es donde inicia la expresion regular)
ExpresionR = []
for j in range (12,len(expresion)):
    ExpresionR.append(expresion[j])

print(expresion)
print(ExpresionR)

