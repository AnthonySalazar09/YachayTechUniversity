#Ejercicios en clase N1:
#2.
'''
x=int(input("Inserte número: "))
if x<0:
    print("Es negativo")
else:
    print("Es positvio")
'''
#3.
'''
x=int(input("Año actual: "))
y=int(input("Año cualquiera: "))
z=x-y
if z<0:
    z*=-1
    print("Faltan",z,"años")
else:
    print("Han pasado",z,"años")
'''
#4
''' 
x=int(input("Ingrese un número del 1 al 3: "))
if x<1 or x>3:
    print("No coincide con los días de la semana")
if x==1:
    print("Lunes")
if x==2:
    print("Martes")
if x==3:
    print("Miércoles")
'''    
#6.
'''
x=int(input("inserte número: "))
y=int(input("inserte número: "))
z=x/y
if (x==0) or (y==0):
    print("No se puede dividir para 0")

elif z%1==0:
    print("es exacta")
else:
    print("no es")
'''
#8.
'''
x=int(input("inserte número: "))
y=int(input("inserte número: "))
if x>y:
    print(x,"es mayor")
if y>x:
    print(y,"es mayor")
elif x==y:
    print("son iguales")
'''
#9.
'''
x=int(input("inserte número: "))
if x%2==0:
    print("par")
else:
    print("impar")
'''
#10.
'''
x=int(input("inserte número: "))
if x%3==0:
    print("Es múlltiplo de 3")
else:
 print("no")
'''
#Guía 1.
#1.
'''
x=input("Ingre roca papel o tijera: ")
y=input("Ingre roca papel o tijera: ")
if x==y:
    print("empate")
elif (x=="roca" and y=="tijera") or (y=="roca" and x=="tijera"):
    print("roca gana a tijera")
elif (x=="tijera" and y=="papel") or (x=="papel" and y=="tijera"):
    print("tijera gana a papel")
elif (x=="roca" and y=="papel") or (x=="papel" and y=="roca"):
    print("papel gana a roca")
else:
    print("Escribiste mal")
'''
#2.
'''
x=int(input("inserte número: "))
y=int(input("inserte número mayor: "))
if x>y:
    print("y debe ser mayor que x")
for i in range(x,y):
    if i%2==0:
        print(i,"par")
    else:
        print(i,"impar")
'''
#3.
'''
x=int(input("inserte número: "))
for i in range(1,x+1):
    if x%i==0:
        print(i,"divisor de", x)
'''
#4.
'''
x=int(input("Cantidad de números: "))
count=0
count1=0
for i in range(x):
    y=int(input("inserte númoers: "))
    if i%2==0:
        count+=1
    else:
        count1+=1
print(count,"números pares")
print(count1,"números impares")
'''
#5.
'''
x=int(input("Cantidad de números: "))
acu=0
for i in range(x):
    y=int(input("Números: "))
    acu+=y
    z=(acu/x)
print(z)
'''
#6.
'''
x=int(input("Temperatura a grado celsius: "))
y=(x*1.8)+32
print(y," grados farenheit")
'''
#7.
'''
from math import sqrt
x1=int(input("inserte númoers: "))
x2=int(input("inserte númoers: "))
y1=int(input("inserte númoers: "))
y2=int(input("inserte númoers: "))
d=sqrt(((x2-x1)**2)+((y2-y1)**2))
print("la distancia es",d)
'''
#8.
'''
x=int(input("inserte númoers: "))
y=int(input("inserte númoers: "))
z=int(input("inserte númoers: "))
a=z-x
if a<0:
    a*=-1
b=z-y
if b<0:
    a*=-1
if a>b:
    print(z,"está mas cerca de",y)
else:
    print(z,"está mas cerca de",x)
'''
#9.
'''
x=int(input("cantidad de números: "))
maxi=0
for i in range(x):
    maxi=0
    y=int(input("Inserte números: "))
    if y>maxi:
     maxi=y
print(maxi)
'''
#10.
'''
x=int(input("cantidad de números: "))
maxi=10000000000000000
for i in range(x):
    maxi=1000000000000
    y=int(input("Inserte números: "))
    if y<maxi:
     maxi=y
print(maxi)
'''
#Práctica 5
#1
'''
maxi=1
mini=100
y=True
while y:
    mid =(maxi+mini)//2
    z=input(str(mid)+" es mayor(1), menor(2) o igual(3) que tu numero? ")
    if z=="1":
        maxi=mid
    elif z=="2":
        mini=mid
    elif z=="3":
        print("Es el número")
        break
'''
#Guía 2.
#|.
'''
x=int(input("Inserte números: "))
y=int(input("Inserte números: "))
z=int(input("Inserte números: "))
if x==y and y==z:
    print("Equilátero")
elif x==y or x==z or y==z:
    print("Isósceles")
else:
    print("Escaleno")
'''
#2.
'''
c=int(input("Medida: "))
if c<=0:
    print("> que 0")
else:   
    cm=c%100
    m=(c//100)%1000
    km=(c//100)//1000
print(c,"centímetros son",km,"km",m,"m",cm,"cm")
'''
#3.
'''
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c=[]
for i in a:
    for j in b:
        if i==j and i not in c:
            c.append(i)
print(c)
'''
#4.
'''
a = [1, 6,1, 2, 3, 5, 8, 13, 21, 34, 55, 89,7,8]
for i in a:
    if 5<i<10:
        print(i)
'''
#5.
'''
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
for i in range(len(a)):
    b.append(a[i])
print(b)
'''
#6.




#Matrices
'''
matriz = []
n=int(input("Cantidad: "))
m=int(input("Cantidad: "))
for i in range(n):
    a=[]
    for j in range(m):
        
        if i%2==0:
            a.append(1)
        else:
            a.append(0)
            
    matriz.append(a)

for i in range(n):
    for j in range(m):
        print(matriz[i][j],end='')
    print()
'''
'''
matriz = []
n=int(input("Cantidad: "))
m=int(input("Cantidad: "))
for i in range(n):
    a=[]
    for j in range(m):
        
        if j%2!=0:
            a.append(1)
        else:
            a.append(0)
            
    matriz.append(a)

for i in range(n):
    print(matriz[i])
'''
'''
matriz=[]
n=int(input("# de Filas: "))
m=int(input("# de Columnas: "))
for i in range(n):
    a=[]
    for j in range(m):
        if (i%2==0):
            if j%2!=0:
                a.append(1)
            else:
                a.append(0)
        else:
            if j%2!=0:
                a.append(0)
            else:
                a.append(1)
    matriz.append(a)

for i in range(n):
    for j in range(m):
        print(matriz[i][j],end="")
    print()
'''
'''
matriz=[]
n=int(input("# de Filas: "))
m=int(input("# de Columnas: "))
for i in range(len(n)):
    a=[]
    for j in range(len(n[i])):
        if (a[i][j]%2==0):
            a.append(1)
        else:
            a.append(0)
    matriz.append(a)
print(matriz)
'''

   
    

