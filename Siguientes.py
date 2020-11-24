#!/usr/bin/env python
#-*-coding utf:-8-*-

def main():
    conjNT=('S','E','L')
    #conjNT=['E','T','F']
    #conjNT=['D','L','T']
    #Reglas={'1':['D','T',"id","L",";"],'2':['L',',','id','L'],'3':['L','@'],'4':["T","float"],'5':["T","int"]}
    #Reglas={'1':["E","E","+","T"],'2':["E","T"],'3':["T","T","*","F"],'4':["T","F"],'5':["F","(","E",")"],'6':["F","id"]}
    Reglas={'1':['S','S',';','S'],'2':['S','id',':=','E'],'3':['S','print','(','L',')'],'4':['E','id'],'5':['E','num'],'6':['E','E','+','E'],'7':['E','(','S',',','E',')'],'8':['L','E'],'9':['L','L',',','E']}
    Siguientes(conjNT,Reglas)

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

    
    for key in Sig:
        #print(key,":",Sig[key])
        print('Siguientes('+key+') = ',Sig[key])
        

if __name__ == '__main__':
	main()