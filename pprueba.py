from tkinter import *
from tkinter import messagebox
from tkinter import font
from PIL import ImageTk,Image
from tkinter.ttk import Notebook,Entry
from tkinter import ttk

def getValue(value):
    print(value)

def getValue2(value):
    print(value)

def Cerrar():
    raiz.destroy()



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

lista = ['id','*','op','+','-','/','(',')','jg','E','T','F']
listaN = ['E','T','F']
listaT = ['id','*','op','+','-','/','(',')','jg']
#----------------------------------------------------Agregar a tabla---------------------------------------------------------------------------#
#---------------------------------------------------tabla construida----------------------------------------------------------------------------#
#tab2
tab1=ttk.Treeview(myframe)
image = Image.open("imagen6.jpg")
image = image.resize((50,35),Image.ANTIALIAS)
bk = ImageTk.PhotoImage(image)
for row in range(15):
    for column in range(len(lista)+1):
        if row==0:
            if (column ==0):
                label=Label(tab1,text="EDO",fg="white",bg="black",compound="center",padx=3,pady=3 )
                label.config(font=('Arial',12))
                label.grid(row=row,column=column,sticky="nsew",padx=1,pady=1)
                tab1.grid_columnconfigure(column,weight=1)
            
            elif (column ==1):
                label=Label(tab1,text="Acción",fg="white",bg="black",compound="center",padx=3,pady=3)
                label.config(font=('Arial',12))
                label.grid(row=row,column=column,sticky="nsew",padx=1,pady=1,columnspan=len(listaT))
                tab1.grid_columnconfigure(column,weight=1)

            elif (column == len(listaT)+1):
                label=Label(tab1,text="Fila",fg="white",bg="black",compound="center",padx=3,pady=3)
                label.config(font=('Arial',12))
                label.grid(row=row,column=column,sticky="nsew",padx=1,pady=1,columnspan=len(listaN))
                tab1.grid_columnconfigure(column,weight=1)
        
        elif row==1:
            if (column ==0):
                label=Label(tab1,bg="black",padx=3,pady=3)
                label.config(font=('Arial',12))
                label.grid(row=row,column=column,sticky="nsew",padx=1,pady=1)
                tab1.grid_columnconfigure(column,weight=1)
            else:
                label=Label(tab1,text=lista[column-1],fg="white",bg="black",padx=3,pady=3)
                label.config(font=('Arial',12))
                label.grid(row=row,column=column,sticky="nsew",padx=1,pady=1)
                tab1.grid_columnconfigure(column,weight=1)


        else:
                if (column ==0):
                    label=Label(tab1,text=str(row-2),fg="white",bg="black",padx=3,pady=3)
                    label.config(font=('Arial',12))
                    label.grid(row=row,column=column,sticky="nsew",padx=1,pady=1)
                    tab1.grid_columnconfigure(column,weight=1)
                
                else:
                    label=Label(tab1,text="  D"+str(4)+"  ",fg="white",bg="black")
                    label.config(font=('Arial',10))
                    label.grid(row=row,column=column,sticky="nsew",padx=1,pady=1)
                    tab1.grid_columnconfigure(column,weight=1)

tab1.pack(fill=BOTH,side=TOP)
bton =Button(mainLabel,text="Cerrar",width=10,command=Cerrar, cursor="hand2")
bton.pack(fill=BOTH)
bton.place(x=495 , y=500)



raiz.mainloop()
