#1.
'''
x=int(input("cantidad de palabras"))
lista=[]
for i in range(x):
    palabras=str(input("Inserte palabra "))
    lista.append(palabras)
print(lista)

lista2=[]
for i in lista:
    lista2=[i]+lista2
print(lista2)
'''
#2.
'''
dig = "0123456789"
cad=input(":")
enc = False
numero= ""
for i in range(len(cad)-12+1):
    numero = cad[i]
    if cad[i]=="0" and cad[i+2]==cad[i+7]=="-":
        num  = False
        for j in range(1,12):
            if j not in [2,7]:
                if cad[i+j] in dig:
                    num=True
                    numero+=cad[i+j]
                else:
                    num = False
                    break
            else:
                numero+="-"
        if num:
            enc = True
            break
        
if enc:
    print(numero)
else:
    print("no encontrado")
'''
'''
x=int(input("ingrese un texto: "))
lista1=["-","0","1","2","3","4","5","6","7","8","9"]
for i in range(len(x)-12):
    count=0
    s=""
    for j in range(1,13):
        if j==1 and x[i+j]=="0":
            count+=1
            s+=x[i+l]
        if count==12:
            break
    count2=0
    if s[0]=="0":
        count2+=1
        print(count2)
    if s[2]=="-":
        count2+=1
        print(count2)
    if s[7]=="-":
        count2+=1
        print(count2)
    if count2==
'''                   
                   

        
        




