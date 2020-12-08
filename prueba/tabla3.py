#!/usr/bin/env python
#-*-coding utf:-8-*-

class Tabla:
    def __init__ (self, indice, Ldestinos):
        self.indice = indice
        self.Ldestinos = Ldestinos
    def __repr__ (self):
        return str(self.indice) + " " + str (self.Ldestinos)

class destinos:
    def __init__ (self, destino, costo):
        self.destino = destino
        self.costo = costo
    def __repr__(self):
        return str(self.costo)

class transicion:
    def __init__ (self, origen, costo, destino):
        self.origen = origen
        self.costo = costo
        self.destino = destino 
    def __repr__ (self):
        return "Ir " + str(self.origen) + " con "+ str(self.costo)+ " a " +str(self.destino)

class gramatica :
    def __init__ (self, origen, derivada):
        self.origen = origen
        self.derivada = derivada
    def __repr__ (self):
        return str (self.origen) + "-> " + str (self.derivada) 

class estados :
    def __init__ (self, numero, conjuntoC):
        self.numero = numero
        self.conjuntoC = conjuntoC
    def __repr__ (self):
        return str (self.numero) + " := " + str (self.conjuntoC)

def convertir_a_estados (lista, diccionario):

    for i in diccionario:
        laux = diccionario[i]
        origen = laux[0]
        derivada = []
        for j in range (1, len(laux)):
            derivada.append(laux[j])
        aux = gramatica (origen, derivada)
        lista.append(aux)

def indice_punto (listaDerivada):
    #regresa la posicion siguiente de donde se encuentra el punto
    for i in range (0, len(listaDerivada)):
        if (listaDerivada[i] == '•'):
            return i+1

def indice_gramatica (LGramatica, X ):
    #regresa la posicion de donde se encuentre la regla gramatical buscara
    for i in range (0, len(LGramatica)):
        if (X == LGramatica[i].origen):
            return i

def poner_punto (derivadas):
    #colocar el punto en una derivada de gramatica nueva
    temp = derivadas.copy()
    temp2 = ['•']
    for i in temp:
        temp2.append (i)

    return temp2

def pertenece_conjunto (a, listaA):
    bandera = 0
    for i in listaA:
        if (i.origen == a.origen):
            if (len(i.derivada) == len(a.derivada)):
                j = 0
                while ( j <  len (i.derivada)):
                    if (i.derivada[j] != a.derivada[j]):
                        break
                    j = j+1
                if (j == len (a.derivada)):
                    bandera = 1
    return bandera 

def pertenece_conjuntoC (conjunto, ListaEstados):
    bandera = 0
    for i in ListaEstados:
        #print (conjunto)
        #print ( i.conjuntoC)
        if (len (i.conjuntoC) == len (conjunto)):
            h = 0
            for j in range (0, len(i.conjuntoC)):
                if (conjunto[h].origen == i.conjuntoC[j].origen):
                    
                    if (len (conjunto[h].derivada) == len (i.conjuntoC[j].derivada)):
                        #print ("lee este de aca " ,conjunto[0])
                        #print (conjunto[j] , "   " , i.conjuntoC[j] )
                        k = 0
                        while (k < len (conjunto[h].derivada) and h < len (i.conjuntoC) ):
                            if (i.conjuntoC[h].derivada[k] != conjunto[h].derivada[k]):
                                break
                            k = k+1
                        if (k == len (conjunto[h].derivada)):
                            bandera = 1
                            #print ("aca hay cambio")
            h = h+1
    #print (bandera, "\n")
    return bandera

def indice_coincidencia (conjunto, Lconjunto):
    indice = -1
    for i in range (0, len (Lconjunto)):
        #print (conjunto)
        #print ( i.conjuntoC)
        if (len (Lconjunto[i].conjuntoC) == len (conjunto)):
            h = 0
            for j in range (0, len(Lconjunto[i].conjuntoC)):
                if (conjunto[h].origen == Lconjunto[i].conjuntoC[j].origen):
                    
                    if (len (conjunto[h].derivada) == len (Lconjunto[i].conjuntoC[j].derivada)):
                        #print ("lee este de aca " ,conjunto[0])
                        #print (conjunto[j] , "   " , i.conjuntoC[j] )
                        k = 0
                        while (k < len (conjunto[h].derivada)):
                            if (Lconjunto[i].conjuntoC[h].derivada[k] != conjunto[h].derivada[k]):
                                break
                            k = k+1
                        if (k == len (conjunto[h].derivada)):
                            indice = i
                            #print ("aca hay cambio")
            h = h+1
    #print (bandera, "\n")
    return indice

def cerradura (Cgramatica, listaNT, LGramatica):
    
    #print ("cerradura")
    for i in Cgramatica:
        #sacar indice donde se encuentra el punto
        aux = indice_punto (i.derivada)  

        if ( aux < len(i.derivada) and i.derivada[aux] in listaNT):
            #sacar indice donde esté la regla de producción no terminal B
            indice = indice_gramatica (LGramatica, i.derivada[aux])

            while ( indice < len(LGramatica) and LGramatica[indice].origen == i.derivada[aux]):
                temp = poner_punto (LGramatica[indice].derivada)
                objetoT = gramatica (LGramatica[indice].origen, temp)

                if (pertenece_conjunto (objetoT, Cgramatica) == 0):
                    Cgramatica.append(objetoT)

                indice = indice +1
    
    return Cgramatica
                
def despuesPunto (lista, x):
    indice = indice_punto (lista.derivada)
    if (indice < len (lista.derivada ) and lista.derivada[indice] == x):
        return 1
    return 0

def actualizar_punto (G):

    temp = []
    i = 0
    while (i < len (G.derivada)):
        if (G.derivada[i] == '•' and i < (len (G.derivada) - 1)):
            temp.append(G.derivada[i+1])
            temp.append (G.derivada[i])
            i = i +1
        else:
            temp.append (G.derivada[i])
        i = i +1
        
    aux = gramatica (G.origen, temp)
    return aux

def Ir_a (I, listaNT, LGramatica, x):
    J = []
    for i in I.conjuntoC:
        if (despuesPunto (i, x) == 1):
            temp = actualizar_punto(i)
            J.append (temp)
    return cerradura(J, listaNT, LGramatica)

def simbolo_gramatical (derivadas):
    indice = indice_punto (derivadas)
    if (indice == len(derivadas)):
        return None

    return derivadas[indice]

def conjunto_vacio (conjunto):
    #regresa un uno si es un conjunto vacio
    #regresa un cero en caso contrario
    if (len(conjunto) > 0):
        return 0
    return 1

def coleccion_canonica (listaNT, LGramatica, Ltransiciones):
    C = []
    temp = gramatica (LGramatica[0].origen, LGramatica[0].derivada.copy() )
    temp.derivada = poner_punto (temp.derivada)
    Ltemp = [temp]
    aux = cerradura (Ltemp, listaNT, LGramatica)
    nuevo = estados(0, aux)
    C.append (nuevo)

    for i in C:
        anterior = ''
        for j in i.conjuntoC:
            x = simbolo_gramatical (j.derivada)

            if (x != None and x!= anterior):
                if (x != '@'):
                   # print ("\nIr_a(", i.numero, "," , x , ")")
                   pass
                if (x == '$'):
                    #print ("aceptacion")
                    nuevoT = transicion (i.numero, x, "acept")
                    Ltransiciones.append (nuevoT)
                
                elif (x !='@'):
                    nuevoConjunto = Ir_a(i, listaNT, LGramatica, x)

                    if (conjunto_vacio(nuevoConjunto) == 0 and pertenece_conjuntoC (nuevoConjunto, C) == 0):
                        nuevoEstado = estados (len (C), nuevoConjunto)
                        C.append (nuevoEstado)
                        nuevoT = transicion (i.numero, x, len(C)-1)
                        Ltransiciones.append (nuevoT)
                        #print (nuevoEstado)

                    elif (conjunto_vacio(nuevoConjunto) == 0):
                        a = indice_coincidencia (nuevoConjunto, C)
                        #print (":= ",a)
                        nuevoT = transicion (i.numero, x, a)
                        Ltransiciones.append (nuevoT)

            anterior = x
    return C

def Siguientes(conjNT,Reglas): #Siguientes(X)
    Sig={}
    for i in range (0,len(conjNT)): #Se inicializa el diccionario de Siguientes
        temp2=[]
        temp=dict(zip([conjNT[i]],[temp2]))
        Sig.update(temp)

    for i in range(0,len(conjNT)): #Inician las reglas
        if (i==0): #Inicio Regla 1
            #print("Se cumple regla 1")
            temp2=['$']
            temp=dict(zip([conjNT[i]],[temp2]))
            Sig.update(temp)
        else:
            for key in Reglas:
                if(conjNT[i]==Reglas[key][1] and len(Reglas[key])==2):
                    temp2=['$']
                    temp=dict(zip([conjNT[i]],[temp2]))
                    Sig.update(temp)   #Fin Regla 1

        for key in Reglas: #Inicio Regla 2
            for j in range(1,len(Reglas[key])):
                if (conjNT[i]==Reglas[key][j]):
                    #print("Se encontró",conjNT[i],"en",key,"posicion:",j)
                    if (len(Reglas[key])>2 and j<=len(Reglas[key])-2):
                        #print("Se cumple la regla 2")
                        #temp=Primeros(Reglas[key][j+1])  --Esta sera la regla una vez implemente Mike Primeros
                        temp2=Reglas[key][j+1]
                        Sig[conjNT[i]].append(temp2)#Fin Regla 2
                    elif(len(Reglas[key])>2 and j==len(Reglas[key])-1 and conjNT[i]!=Reglas[key][0]): #Inicio Regla 3
                        #print("Se cumple la regla 3")
                        temp2=Sig[Reglas[key][0]]
                        for n in range(0,len(temp2)):
                            #print('entra')
                            if ((temp2[n] in Sig[conjNT[i]]) == False):
                                #print('Entra2')
                                temp=temp2[n]
                                Sig[conjNT[i]].append(temp)
    return Sig
    
def BuscarT(origen,costo,listaT):
    for i in listaT:
        if i.origen == origen and i.costo == costo:
            return i.destino
    return -1

def hallar_reduccion (Conjunto, sig, reglas, Lista):
    for i in Conjunto:
        a =indice_punto(i.derivada)
        if ( a == len(i.derivada) or i.derivada[a] == '@') :
            copia = []
            copia.append(i.origen)
            for j in i.derivada:
                copia.append(j)
            if ('@' in i.derivada):
                 copia.pop()
                 copia.pop ()
                 copia.append (i.derivada[a])
            else:
                copia.pop() #sacar el ultimo elemento porque es •

            for key in reglas:
                if (copia == reglas[key]):
                    for m in sig:
                        if (i.origen == m):
                            for k in sig[m]:
                                Lista.append (k)
                    return key
    return -1

            

def Crear_Tabla (ListaColeccion, ListaTransiciones, ListaT, ListaNT, sig, reglas):
    ListaTabla = []
    for i in ListaColeccion:
        Ld = []
        Lr = []
        indice = hallar_reduccion (i.conjuntoC, sig, reglas, Lr)
        #print (i.numero, indice)
        #print (Lr)
        
        for j in ListaT:
            if (j in Lr and indice != -1):
                nuevaD = destinos (j, "r"+str(indice))
                Ld.append (nuevaD)
            else:
                a  = BuscarT (i.numero, j, ListaTransiciones)
                if (a != -1):
                    nuevaD = destinos (j, "d"+str(a))
                    Ld.append (nuevaD)
                else:
                    nuevaD = destinos (j, "none")
                    Ld.append (nuevaD)
    
        #poner el de pesos
        if (i.numero == 1):
            nuevaD = destinos ('$', "acept")
            Ld.append (nuevaD)
        elif ('$' in Lr and indice != -1):
            nuevaD = destinos ('$', "r"+str(indice))
            Ld.append(nuevaD)
        else:
            nuevaD = destinos ('$', "none")
            Ld.append (nuevaD)

        for j in ListaNT:
            a = BuscarT(i.numero, j, ListaTransiciones)
            if (a != -1):
                nuevoD = destinos (j, str(a))
                Ld.append (nuevoD)
            else:
                nuevoD = destinos (j, "none")
                Ld.append (nuevoD)

        nuevoT = Tabla (i.numero, Ld)
        ListaTabla.append (nuevoT)
    return ListaTabla
            

def imprimirG(listaP,listaT,listaNT):
    def Cerrar():
        raiz.destroy()

    def unir(l1,l2):
        l0=[]
        for i in range(0,len(l1)):
            l0.append(l1[i])
        for i in range(0,len(l2)):
            if i == 0:
                l0.append("$")
                l0.append(l2[i])
            else:
                l0.append(l2[i])
        
        return l0
    
    raiz = Tk()
    raiz.resizable(0,0)
    raiz.title("prueba")
    raiz.geometry("1080x600")
    image2 =Image.open("fondo5.jpg")
    background_image = ImageTk.PhotoImage(image2)
    mainLabel = Label(image=background_image)
    mainLabel.place(x=0, y=0, relwidth=1, relheight=1)
    #------------------------------------------------table-----------------------------------------------------------------------------------------#
    tablayaut = LabelFrame(raiz)
    tablayaut.pack(fill="both",expand=1)
    tablayaut.place(y=90,x=350,height=350,width=400)
    #------------------------------------------------Scrolls-----------------------------------------------------------------------------------------#
    c=Canvas(tablayaut)
    c.pack(side="left",fill="both",expand=1)

    yscrollbar= ttk.Scrollbar(tablayaut, orient=VERTICAL,command=c.yview,cursor="sb_v_double_arrow")
    yscrollbar.pack(side=RIGHT,fill=Y)

    xscrollbar = ttk.Scrollbar(mainLabel, orient=HORIZONTAL,command=c.xview,cursor="sb_h_double_arrow")
    xscrollbar.pack(side=BOTTOM,fill=X)
    xscrollbar.place(y=440,x=347,width=400)

    c.configure(yscrollcommand=yscrollbar.set, xscrollcommand=xscrollbar.set)  

    c.bind('<Configure>',lambda e: c.configure(scrollregion = c.bbox("all")))

    myframe = Frame(c)
    c.create_window((0,0),window=myframe,anchor='nw')

    #listaP = ['id','*','op','+','-','/','(',')','jg','E','T','F']
    #listaNT = ['E','T','F']
    #listaT = ['id','*','op','+','-','/','(',')','jg']
    #----------------------------------------------------Agregar a tabla---------------------------------------------------------------------------#
    #---------------------------------------------------tabla construida----------------------------------------------------------------------------#
    #print(listaT)
    #print(listaNT)
    #tab2
    listaU = unir(listaT,listaNT)
    print(len(listaU))
    print(len(listaP[0].Ldestinos))
    tab1=ttk.Treeview(myframe)
    #print(len(listaU))
    #print(len(listaP[0].Ldestinos))
    #print(listaP[0].Ldestinos)
    for row in range(0,len(listaP)+2):
        for column in range(len(listaP[0].Ldestinos)+1):
            if row==0:
                if (column ==0):
                    label=Label(tab1,text="EDO",fg="white",bg="black",compound="center",padx=3,pady=3 )
                    label.config(font=('Arial',12))
                    label.grid(row=row,column=column,sticky="nsew",padx=1,pady=1)
                    tab1.grid_columnconfigure(column,weight=1)
            
                elif (column ==1):
                    label=Label(tab1,text="Acción",fg="white",bg="black",compound="center",padx=3,pady=3)
                    label.config(font=('Arial',12))
                    label.grid(row=row,column=column,sticky="nsew",padx=1,pady=1,columnspan=len(listaT)+1)
                    tab1.grid_columnconfigure(column,weight=1)

                elif (column == len(listaT)+2):
                    label=Label(tab1,text="Ir_a",fg="white",bg="black",compound="center",padx=3,pady=3)
                    label.config(font=('Arial',12))
                    label.grid(row=row,column=column,sticky="nsew",padx=1,pady=1,columnspan=len(listaNT))
                    tab1.grid_columnconfigure(column,weight=1)
        
            elif row==1:
                if (column ==0):
                    label=Label(tab1,bg="black",padx=3,pady=3)
                    label.config(font=('Arial',12))
                    label.grid(row=row,column=column,sticky="nsew",padx=1,pady=1)
                    tab1.grid_columnconfigure(column,weight=1)
                else:
                    label=Label(tab1,text=listaU[column-1],fg="white",bg="black",padx=3,pady=3)
                    label.config(font=('Arial',12))
                    label.grid(row=row,column=column,sticky="nsew",padx=1,pady=1)
                    tab1.grid_columnconfigure(column,weight=1)

            elif row > 1:
                if(column==0):
                    label=Label(tab1,text=row-2,fg="white",bg="black")
                    label.config(font=('Arial',10))
                    label.grid(row=row,column=column,sticky="nsew",padx=1,pady=1)
                    tab1.grid_columnconfigure(column,weight=1)

                else:
                    label=Label(tab1,text=listaP[row-2].Ldestinos[column-1],fg="white",bg="black")
                    label.config(font=('Arial',10))
                    label.grid(row=row,column=column,sticky="nsew",padx=1,pady=1)
                    tab1.grid_columnconfigure(column,weight=1)

    tab1.pack(fill=BOTH,side=TOP)
    bton =Button(mainLabel,text="Cerrar",width=10,command=Cerrar, cursor="hand2")
    bton.pack(fill=BOTH)
    bton.place(x=495 , y=500)
    raiz.mainloop()


def main ():
    Reglas={}
    Reglas2={}
    aux=[]
    cont = 0
    f = open("Ejemplo.txt")
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

    #print(cadenas)
    #print(cadenas2)
    #---------------------------------------------------------------------------------------------------#
    #Pasar a diccionarios  
    #1
    for i in range (0,len(cadenas)):
        num=str(i+1)
        cadena=" ".join(cadenas[i])
        valor=cadena.split(sep=" ")
        dicci=dict(zip([num],[valor]))
        Reglas.update(dicci)

    #for key in Reglas:
    #    print(key,":",Reglas[key])
    #print("Reglas 2")
    #2
    for j in range (0,len(cadenas2)):
        num2=str(j)
        cadena2=" ".join(cadenas2[j])
        valor2=cadena2.split(sep=" ")
        dicci2=dict(zip([num2],[valor2]))
        Reglas2.update(dicci2)


    #for key2 in Reglas2:
    #    print(key2,":",Reglas2[key2])

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
                    if p < 64 or p > 90 :
                        terminales.append(cadenas[i][j])
    conjNT=[]
    for m in range(0,len(Nterminales)):
        if((Nterminales[m] in conjNT)==False):
            conjNT.append(Nterminales[m])
    print(Nterminales)
    print(terminales)
    Ntermin = []
    termin = []
  
    for i in Nterminales:
        if i not in Ntermin:
            Ntermin.append(i)

    for i in terminales:
        if i not in termin:
            termin.append(i)

    print(Ntermin)
    print (termin)
    listaNT = Ntermin
    listaT = termin

    #listaT = ["id", '+', '*', '(', ')']
    #listaNT=['E','T','F']
    #Reglas2={'1':["E","E","+","T"],'2':["E","T"],'3':["T","T","*","F"],'4':["T","F"],'5':["F","(","E",")"],'6':["F","id"]}
    #Reglas={'0':["E'", "E", "$"],'1':["E","E","+","T"],'2':["E","T"],'3':["T","T","*","F"],'4':["T","F"],'5':["F","(","E",")"],'6':["F","id"]}
    #listaNT=['D','L','T']
    #listaT = ["id", ';', ',', '@', 'float','int']
    #Reglas={'0': ["D'", "D", "$"], '1':['D','T',"id","L",";"],'2':['L',',','id','L'],'3':['L','@'],'4':["T","float"],'5':["T","int"]}
    #Reglas2={'1':['D','T',"id","L",";"],'2':['L',',','id','L'],'3':['L','@'],'4':["T","float"],'5':["T","int"]}
    LGramatica = []
    convertir_a_estados (LGramatica, Reglas2)
    Ltransiciones = []
    C = coleccion_canonica (listaNT, LGramatica, Ltransiciones)
    sig = Siguientes (listaNT, Reglas2)
    listaTabla = Crear_Tabla (C, Ltransiciones, listaT, listaNT, sig, Reglas)
    for i in listaTabla:
        print(i)
    imprimirG(listaTabla,listaT,listaNT)
    

if __name__ == '__main__':
    import PySimpleGUI as sg
    from tkinter import filedialog
    import os
    from tkinter import *
    from tkinter import messagebox
    from tkinter import font
    from PIL import ImageTk,Image
    from tkinter.ttk import Notebook,Entry
    from tkinter import ttk 
    main ()