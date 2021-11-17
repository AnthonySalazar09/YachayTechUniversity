#1.
'''
def suma(a,b):
    z=a+b
    print(z)

print(suma(1,2))
z1=suma(1,2)
print(z1)
x1=5
x2=6
z2=suma(x1,x2)
print(z2)
'''

'''
a=[1,2,3,4,5]
def Fact(a):

    return()
for i in range(len(a)):
    print(Fact(a[i])
'''
'''
def crearlista(x1):
    a=[]
    for i in range(x1):
        y=int(input("ingrese valores="))
        a.append(y)
    return a
b=crearlista(int(input("ingrese tamaño de lista")))
print(b)
c=crearlista(5)
print(c)
'''
#Matrices
#Suma de matrices
'''
a=[[1,1,1],[1,1,1],[1,1,1]]
b=[[2,2,2],[2,2,2],[2,2,2]]
for i in range(len(a)):
    for j in range(len(a[i])):
        a[i][j]=a[i][j]+b[i][j]
print(a)
'''
#Recorrer matrices
'''
a=[[1,2,3],[4,5,6],[7,8,9]]
b=[[1,2,3],[4,5,6],[7,8,9]]
for i in range(len(a)):
    for j in range(len(a[i])): 
        print(a[i][j])
'''
#Añadir filas
'''
a=[[1,2,3],[4,5,6],[7,8,9]]
b=[[1,2,3],[4,5,6],[7,8,9]]
a.append([1,2,3])
print(a)
'''
#Hacer una Matriz
'''
a=int(input("ingrese tamaño de filas "))
b=int(input("Ingrese tamaño de Columnas "))
c=[]
for i in range(a):
    aux=[]
    for j in range(b):
        z=int(input("Ingrese elementos"))
        aux.append(z)
    c.append(aux)
print(c)
'''
#Realizar y sumar dos matrices
'''
a=int(input("ingrese tamaño de filas "))
b=int(input("Ingrese tamaño de Columnas "))
def crearmatriz(a,b):
    c=[]
    for i in range(a):
        aux=[]
        for j in range(b):
            z=int(input("Ingrese elementos"))
            aux.append(z)
        c.append(aux)
    return c
z1=crearmatriz(a,b)
print(z1)
z2=crearmatriz(a,b)
print(z2)
def sumarmatriz(x1,x2):
    for i in range(len(x1)):
        for j in range(len(x1[i])):
            x1[i][j]=x1[i][j]+x2[i][j]
    return x1
z3=sumarmatriz(z1,z2)
print(z3)
'''
#Crear matriz de manera rápida
'''
c=[]
for i in range(2):
    a=[0]*3
    c.append(a)
print(c)

for i in range(len(c)):
    for j in range(len(c[i])):
        c[i][j]=int(input("ingrese valor="))
print(c)
'''
'''
c=[]
for i in range(2):
    a=[0]*3
    c.append(a)
print(c)
for i in range(len(c)):
    for j in range(len(c[i])):
        c[i][j]=int(input("Elemento[%d][%d]="%(i,j)))
print(c)

print("hola %d"%(11))
'''

#Otra manera de crear una matriz
'''
a=[[1,2,3],[4,5,6],[7,8,9,]]
c=[]
count=1
for i in range(3):
    aux=[]
    for j in range(3):
        aux.append(count)
        count+=1
    c.append(aux)
print(c)
'''
a=[[1,2,3],[4,5,6],[7,8,9,]]
c=[]
for i in range(3):
    c.append([0]*3)
print(c)
count=1
for i in range(len(a)):
    for j in range(len(a[i])):
                   c[i][j]=count
                   count+=1
print(c)
                   

