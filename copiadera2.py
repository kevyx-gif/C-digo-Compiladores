import sys
import difflib
#---------------------------------------------------------------------------------------------------------------------------------------------#
#FUNCIONES
def union(elem1, elem2):
	ini=elem1
	fin=elem2
	in1=pila_I.pop()
	in2=pila_I.pop()     
	f1=pila_F.pop()
	f2=pila_F.pop()
	inicio=ini
	f=fin
	lista_Trans.append([str(inicio),'@',str(in1)])
	lista_Trans.append([str(inicio),'@',str(in2)])
	lista_Trans.append([str(f1),'@',str(f)])
	lista_Trans.append([str(f2),'@',str(f)])
	pila_I.append(inicio)
	pila_F.append(f)

#-----------------------------------------------------------------------------------------------------------------------------------------------#
def klean(elem1, elem2):
	ini=elem1
	fin=elem2
	 
	ini1=pila_I.pop()
	fin1=pila_F.pop()

	lista_Trans.append([str(ini),'@',str(fin)])
	lista_Trans.append([str(ini),'@',str(ini1)])
	lista_Trans.append([str(fin1),'@',str(ini1)])
	lista_Trans.append([str(fin1),'@',str(fin)])
	
	pila_I.append(ini)
	pila_F.append(fin)

#-----------------------------------------------------------------------------------------------------------------------------------------------#

def posit(elem1, elem2):
	ini=elem1
	fin=elem2
	ini1=pila_I.pop()
	fin1=pila_F.pop()

	lista_Trans.append([str(ini),'@',str(ini1)])
	lista_Trans.append([str(fin1),'@',str(ini1)])
	lista_Trans.append([str(fin1),'@',str(fin)])

	pila_I.append(ini)
	pila_F.append(fin)

#-----------------------------------------------------------------------------------------------------------------------------------------------#

def sust (elem1, elem2):
    for i in lista_Trans :
        if (i[0] == str(elem2)):
            i[0] = str(elem1)

#-----------------------------------------------------------------------------------------------------------------------------------------------#

def conc():
	ini1=pila_I.pop()
	ini2=pila_I.pop()
	fin1=pila_F.pop()
	fin2=pila_F.pop()
	sust(fin2,ini1)
	pila_I.append(ini2)
	pila_F.append(fin1)

#-----------------------------------------------------------------------------------------------------------------------------------------------#

def thompson (cadena):
    cont = 0
    cont2 = 1
    for c in cadena:
        if ((ord(c)>=97 and ord(c)<=122) or (ord(c)>=65 and ord(c)<=90) or (ord(c)>=48 and ord(c)<=57)):
            lista_Trans.append([str(cont), c, str(cont2)])
            pila_I.append(cont)
            pila_F.append(cont2)
            cont = cont+2
            cont2 = cont2+2

        elif ( c == '*'):
            klean(cont, cont2)
            cont =cont+2
            cont2 = cont2+2

        elif (c == '/'):
            union(cont, cont2)
            cont = cont+2
            cont2 = cont2+2
        
        elif (c == '+'):
            posit(cont, cont2)
            cont = cont +2
            cont2 = cont2 +2

        elif (c == '-'):
            conc ()

#-----------------------------------------------------------------------------------------------------------------------------------------------#
#Comienzo del programa

lpos = []
alfabeto = []
pila = ['n']

expresion = "asa"
#-----------------------------------------------------------------------------------------------------------------------------------------------#
#Sacar de archivo
contador = 0
f = open("prueba.txt")
        #poner nombre del archivo que se va a abrir
for linea in f:
    if contador == 0:
        contador = contador + 1

    else: 
        expresion = linea           
f.close()
#-----------------------------------------------------------------------------------------------------------------------------------------------#
#Convertir lista a string
ExpresionR = []
for j in range (12,len(expresion)):
    ExpresionR.append(expresion[j])

expresion = ExpresionR
#-----------------------------------------------------------------------------------------------------------------------------------------------#
#Procedimiento
for i in expresion:

    if ( (ord(i)>= 65 and ord(i) <= 90) or (ord(i)>= 97 and ord(i)<= 122)):
        lpos.append(i)
        alfabeto.append (i)
    else:
        if (pila == [] or pila[len(pila)-1] == '(' or i == '(' ):
            pila.append(i)
        elif (i == '+' or i == '*'):
            if (pila[len(pila)-1] == '+' or pila[len(pila)-1] == '*'):
                lpos.append(i)
            else:
                pila.append(i)
        elif (i == '-'):

            while (pila[len(pila)-1] == '+' or pila[len(pila)-1] == '*'):
                lpos.append(pila.pop())

            if (pila[len(pila)-1] =='-'):
                lpos.append(i)
            else:
                pila.append (i)

        elif (i == '/'):

            while (pila[len(pila)-1] == '+' or pila[len(pila)-1] == '*' or pila[len(pila)-1] == '-'):
                lpos.append(pila.pop())
            if (pila[len(pila)-1] == '/'):
                lpos.append (i)
            else:
                pila.append(i)

        else:
            while (pila[len(pila)-1] != '('):
                lpos.append (pila.pop())
            pila.pop()

while (len(pila) > 1):
    lpos.append(pila.pop())

for j in range (len(alfabeto)-1, -1, -1):
    if (alfabeto[j] in alfabeto[:j]):
        del(alfabeto[j])

#-----------------------------------------------------------------------------------------------------------------------------------------------#
#invocacion del generador de automata
lista_Trans = []
pila_I = ['n']
pila_F = ['n']


thompson(lpos)
#-----------------------------------------------------------------------------------------------------------------------------------------------#

print ('a')
print (alfabeto)

print ('p')
print (lpos)

print ('t')
print (lista_Trans)
print ('afn')
print (pila_I)
print (pila_F)
print ('e')