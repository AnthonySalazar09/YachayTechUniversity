
'''
a=int(input("Ingrese una lista: "))
A=list(a)
print(A)
'''
#Práctica N#7
#1. Programa para hacer el ordenamiento de burbuja
'''
lista=[2,4,6,3,1]
for i in range(len(lista)):
    for j in range(i,len(lista)):
        if lista[j]<lista[i]:
            aux=lista[j]
            lista[j]=lista[i]
            lista[i]=aux
print(lista)
'''
#1.Progama para poner la lista en orden creciente
'''
a=[5,6,7,8,2,3,4]€
for i in range(len(a)): 
    for j in range(i,len(a)):
       if a[j]<a[i]:
           aux=a[i]
           a[i]=a[j]
           a[j]=aux
print(a)
'''
#2.Progama para poner la lista en orden decreciente
'''
a=[5,6,7,8,2,3,4]
for i in range(len(a)):
    for j in range(i,len(a)):
       if a[j]>a[i]:
           aux=a[i]
           a[i]=a[j]
           a[j]=aux
print(a)
'''
#3.
'''
c1=str(input("Texto: "))
c2=str(input("Texto2: "))
c3=""
c3=c1[0]+c1[1]+c2[-1]+c2[-2]
print(c3)
'''
#4.
'''
x1=input("ingrese texto: ")
x2=input("ingrese caracter: ")
x1=list(x1)
print(x1)
print(x2)
for i in range(len(x1)):
    if x1[i]==x2:
        x1[i]="$"
print(x1)

x3=""
for i in range(len(x1)):
    x3=x3+x1[i]
print(x3)
'''

'''
x1=input("ingrese texto: ")
x2=input("ingrese caracter: ")
x3=""
for i in x1:
    if i==x2:
        x3=x3+"$"
    else:
        x3=x3+i
print(x3)
'''
#5.

a=["rojo","blanco","negro","rojo","verde","negro"]
b=[]
for i in range(len(a)):
    if a[i] not in b:
        b.append(a[i])
print(b)

'''
x="rojo,blanco,negro,rojo,verde,negro"
count=0
z=" "
lista[]
while count<len(x):
    if x[count]!=",":
        z=z+x[count]
    else:
        lista.append(z)
        z=""
    count+=1
print(lista)
lista2=[]
for i in range(len(lista)):
    íf lista[i] not in lista2:
        lista2.append(lista[i])
print(lista2)
x3=" "
for i in range(len(lista2)):
    x3=x3+lista2[i]
    if i!=len(lista2)-1:
    x3=x3+","
print(x3)
'''
#6.
'''
x=input("Ingrese dígitos: ")
lista=list(x)
print(lista)
for i in range(len(lista)):
    if lista[0]==0:
     print(lista)
    else:
     print("No")
'''
#7.
'''
x=str(input("Ingrese palabra: "))
lista=list(x)
for i in range(len(lista)):
    lista[0]=lista[0].upper()
    lista[-1]=lista[-1].upper()
print(lista)
'''    
