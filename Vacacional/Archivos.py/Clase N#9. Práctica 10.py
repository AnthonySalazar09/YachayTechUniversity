#Clase N#9. Práctica 10
#2.
'''
n=int(input("Ingrese dimensión: "))
c=[]
for i in range(n):
    c.append([0]*n)
print(c)

for i in range(len(c)):
    for j in range(len(c[i])):
        if i==j:
            c[i][j]=1
print(c)
'''
#3.
'''
n=int(input("Fila: "))
m=int(input("Columna: "))
c=[]
for i in range(n):
    c.append([0]*m)
print(c)
        
for i in range(len(c)):
    for j in range(len(c[i])):
                c[i][j]=i*j
print(c)
'''
'''
n=int(input("Fila: "))
m=int(input("Columna: "))
c=[]
for i in range(n):
    a=[]
    for j in range(m):
        a.append(i*j)
    c.append(a)
print(c)
'''
#4.
'''
from random import randint
x=randint(0,10)
def crearmatriz(n,m):
    c=[]
    for i in range(n):
        c.append([0]*m)    
    for i in range(len(c)):
        for j in range(len(c[i])):
           c[i][j]=randint(0,9)
    return c
x1=int(input("Filas: "))
x2=int(input("Columnas "))
z1=crearmatriz(x1,x2)
z2=crearmatriz(x1,x2)
z3=crearmatriz(x1,x2)

for i in range(len(z3)):
    for j in range(len(z3[i])):
        z3=[i][j]=z1[i][j]+z2[i][j]

print(z1)
print(z2)
print(z3)
'''
#
'''
for i in range(len(x1)):
    for j in range(len(m1[i]):
        print(m1[i][j],end='\'t')
    print('\n')
'''
#Guía
#3.
'''
x=[1,5,-2.-4]
lista1=[]
for i in range(len(x)):
    for j in range(len(x)):
        if i!=j:
            c=x[i]*x[j]
            lista1.append(c)
print(lista1)
mayor=lista1[0]
for i in range(len(lista1)):
    if mayor <lista1[i]:
        mayor=lista1[i]
print(mayor)
'''


#5.

lista=["a","e","i","o","u"]
def eje(x,y):
    resultados=""
    if y=="v":
        for i in x:
            if i in lista:
                resultados+=i
    return resultados
z=eje("algoritmos","v")
print(z)

