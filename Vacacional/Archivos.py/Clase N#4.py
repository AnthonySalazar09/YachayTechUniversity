#Clase N#4
#Escriba un programa que muestre un mensaje cada vez que un numera no sea mayor que el primero
'''
x=int(input("ingrese un numero"))
y=int(input("ingres un dato"))
for i in range(x-1):
    z=int(input("ingrese un número"))
    if z<=y:
        print(z,"no es mayor que el primero")
'''
#Escriba un programa que escriba cuántos negativos ha introducido
'''
x=int(input("Cantidad de números"))
count=0
for i in range(x):
    z=int(input("Números: "))
    if z<0:
        count+=1
print("hay",count,"números negativos") 
'''
#Juego donde tenga que adivinar un número que se genere, indicar si es correcta, mayor o menor
'''
from random import randint
x=randint(0,10)
for i in range(0,1000):
    y=int(input("Ingrese su número"))
    if y<x:
        print(y,"es menor que x")
    elif y>x:
        print(y,"es mayor que x")
    elif y==x:
        print("adivinaste el número alfin xd")
        break
'''
#Escriba un programa que solicite un numero. Este numero sera la secuencia de la serie fibonacci.
'''
x=int(input("ingrese un número"))
t1= 0
t2= 1
print(t1)
print(t2)

for i in range(x-2):
    y=t1+t2
    t1=t2
    t2=y
    print(y)
'''
#Escriba un programa que pida un número entero mayor que 1 y que escriba si el número es primo o no
'''
x=int(input("ingrese número"))
count=0
for i in range(1,x+1):
    if x%i==0:
       count+=1
    if count ==2:
       print("es primo")
    else:
        print("no es primo")
'''
#Calcule cuantos terminos debo de sumar para tener una suma total >=1000
'''
count=0
for i in range(1,1000):
    count+=i
    if count>=1000:
       break
print(i)
'''
#Escriba un progrma que pida dos números entereos y escriba la suma de todos los enteroes desde el primer número hasta el segundo
'''
x=int(input("ingrese número"))
y=int(input("ingrese número mayor que el anterior"))
count=0
for i in range(x,y+1):
     count+=i
print(count)
'''
      
  
    
    




        
    
