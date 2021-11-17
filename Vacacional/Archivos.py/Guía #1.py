#Guía 1
#1.
'''
jugador1=input("Elige roca, papel o tijera: ")
jugador2=input("Elige roca, papel o tijera: ")
if jugador1==jugador2:
    print("es un empate")
elif (jugador1=="roca" and jugador2=="tijera") or (jugador2=="roca" and jugador1=="tijera"):
    print("roca gana a tijera")
elif (jugador1=="tijera" and jugador2=="papel") or (jugador2=="tijera" and jugador1=="papel"):
    print("tijera gana a papel")
elif (jugador1=="papel" and jugador2=="roca") or (jugador2=="papel" and jugador1=="roca"):
    print("papel gana a roca")
else:
   print("Lo ingresaron mal")
'''
#2.
'''
x=int(input("Número entero: "))
y=int(input("Número mayor que el primero: "))
if y<x:
   print("No es mayor que el primero")
for i in range(x,y):
    if i%2==0:
        print(i,"es par")
    else:
        print(i,"es impar")
'''
#3.
'''
x=int(input("Insertar un número mayor que 0: "))
y=int(input("Insertar número: "))
for i in range(1,x+1):
    if x<=0:
        print("debe ser mayor")
    else:
        print(y,"/",i,"=",y/i)
'''
#4.
'''
x=int(input("cantidad de números"))
count1=0
count2=0
for i in range(x+1):
    num = float(input("numero:"))
    if num%2==0:
       count1+=1
       print(num,"es par")
    elif num%2!=0:
       count2+=1
       print(num,"es impar")
            
print("hay",count1," números pares")
           
print("hay",count2," números inpares")
'''                    

#5.
'''
x=int(input("Cantidad de números"))
acu = 0
for i in range(x):
   num = float(input("numero:"))
   acu += num
print(acu/x)
'''
#6.
'''
x=int(input("Temperatura a grado celsius: "))
y=(x*1.8)+32
print(y," grados farenheit")
'''
#7.
'''
import math
x1=int(input("Inserte número"))
x2=int(input("Inserte número"))
y1=int(input("Inserte número"))
y2=int(input("Inserte número"))
d=math.sqrt(((x2-x1)**2)+((y2-y1)**2))
print("la distancia entre estos dos puntos es ",d)
'''
#8.
'''
x=int(input("Inserte número"))
y=int(input("Inserte número"))
z=int(input("Inserte número"))
a=z-x
if a<0:
   a*=-1
b=z-y
if b<0:
   b*=-1
if a>b:
       print(z, "está mas lejos de",y)
else:
        print(z, "esta mas cerca de ",x)
'''

#9.
'''
x=int(input("Cantidad de números"))
maxi = 0
for i in range(x):
   num = float(input("numero:"))
   if num>maxi:
       maxi=num
print(f"{maxi} es el mayor número")
'''
#10.
'''
x=int(input("Cantidad de números"))
maxi = 10000000000000
for i in range(x):
   num = float(input("numero:"))
   if num<maxi:
       maxi=num
print(f"{maxi} es el número menor ")
'''
'''
x=int(input("inserte número: "))
for i in range(1,x+1):
    if x%i==0:
        print(i,"divisor de", x)
'''
#9 con while.

x=int(input("numero: "))
count=0
maxi=0
while count<x:
    num=int(input(""))
    if num>maxi:
        maxi=num
    count+=1
    
        




