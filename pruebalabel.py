from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import font
from PIL import ImageTk,Image
from tkinter.ttk import Notebook,Entry
from tkinter import ttk 

def abrir():
    Reglas ={}
    Reglas2 = {}
    auxx2=[]
    auxx =[]
    cont = 0
    archivo=filedialog.askopenfile()
    lines = archivo.read()
    for linea in lines:
        if cont != 0:
            if linea == "\n":
                auxx3 = linea.replace('\n',' ')
                auxx.append(auxx3)
                auxx4=auxx.copy()
                auxx2.append(auxx4)
                del auxx[:]
            else:
                auxx.append(linea)

        
        elif linea=="\n":
            cont = cont +1 
    auxx5=[]
    for i in auxx2:
        auxx6="".join(i)
        auxx5.append(auxx6)
    print(auxx5)
    #-----------------------------------------------------------------------------------------------#
    letraAux = auxx5[0][0]
    ax = auxx5.copy()
    ax.insert(0,letraAux+' -> '+letraAux+' $ ')
    #---------------------------------------------------------------------------------------------------#
    #Lmpieza
    cadenas = []
    aux2 = []
    aux3 = []
    for i in range(0,len(auxx5)):
        for j in range(0,len(auxx5[i])):
            if auxx5[i][j] == " ":
                aux4 = "".join(aux3)
                aux2.append(aux4)
                del aux3[:]
            
            else:
                aux3.append(auxx5[i][j])
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
ventana=Tk()
ventana.resizable(0,0)
image2 =Image.open("fondo3.jpg")
background_image = ImageTk.PhotoImage(image2)
mainLabel = Label(image=background_image)
mainLabel.place(x=0, y=0, relwidth=1, relheight=1)
ventana.geometry("300x100")

botonAbrir=Button(ventana,text="Seleccionar archivo", command=lambda : abrir())
botonAbrir.place(x=85,y=30)
ventana.mainloop()