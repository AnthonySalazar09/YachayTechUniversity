
lista=[]

while True:
    Error=True
    n=input("Ingrese su número telefónico: ")
    lista=[int(i)for i in n]
    #print(lista)
    for i in range(1):
        if lista[0]==0:
            Error= False
            break
    if Error==False:
        x=""
        for i in range(len(lista)):
            if i==2 or i==6:
                 x=x+"-"+n[i]
            else:
                x=x+n[i]
        print(x,end="")
        print()
        break
        
    if Error==True:
        print("No es válido. Ingrese nuevamente: ")

##    if Error==False:
##        x=""
##        for i in range(len(lista)):
##            if i==2 or i==6:
##                x=x+"-"+n[i]
##            else:
##                x=x+n[i]
##        print(x,end="")
##    print()
    #break

        
