#Práctica 3
#Ejercicio 1.
'''
x=int(input("cantidad de palabras"))
lista=[]

for i in range(x):
    palabras=str(input("Inserte palabra "))
    lista.append(palabras)
print(lista)
buscar=str(input("Palabra que quieras buscar: "))
count=0
for i in range(len(lista)):
    if i==buscar:
        count+=1
print("la palabra",buscar,"se repite", count)
'''
#Ejercicio 2.
    
x=int(input("Cantidad de palabras: "))

if x<1:
    print("No se puede")
else:
    a= []
    for i in range(x):
        y=input("diagme la palabra: ")
        a+=[y]
    print(a)
    z= input("Sustituir la palabra: ")
    w= input("por la palabra: ")
    for i in range(len(a)):
        if a[i] ==z:
            a[i]=w
    print("La lista es ahora:", a)



