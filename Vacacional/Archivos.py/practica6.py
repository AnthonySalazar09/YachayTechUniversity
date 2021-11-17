# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 11:48:36 2019

@author: hp
"""

###17-1-811040-4
###21-2 1

###si un numero es mayor que 10 restarle 9
###la suma aplicarle el modulo 6
'''
n = input("ingrese numero de cedula")
lista = list(n)
###print(lista)
for i in range(len(lista)):
    lista[i]= int(lista[i])
###print (lista)    
x= lista[len(lista)-1]
print(x, end=" ")
###print(x)
lista2=[2,1,2,1,2,1,2,1,2]
lista3=[]
s=0
for i in range(9):
    e = lista[i]*lista2[i]
    if e>=10: 
        e=e-9
        lista3=lista3 + [e]
    else:
        lista3=lista3 + [e]
    s=s+e
r= s % 10
print(r)

if r == 0:
    print("cedula correcta")
elif x == r:
    print("cedula correcta")
else:
    print("cedula incorrecta")

print(s)
print(lista3)
'''


'''
###ejercicio 2
array = [1, 1,3,4,5]

count= 0
for i in range(len(array)-1):
    if array[i]%2==0:
        count = count +1
print(count)
'''
'''
###ejercicio3
array = [1,2,1,4,5]
max = array[0]
min = array[0]
for i in range(len(array)):
    if array[i]>= max:
        max = array[i]
print (max)

for j in range(len(array)):
    if array[j] <= min:
        min = array[j]
print (min)
dif = max - min
print(dif)
'''
###ejercicio4
###lista = ["steven", "juan", "123"]
###print(len(lista[0]))
###print ( lista[0][0])

###implementar for para ingresar str a la lista
'''
lista= ["steven", "juan", "1231", "33", "donad", "jjj"]
###a= len(lista[0])
###print(lista[0][a-1])
count= 0
for i in range(len(lista)):    
    a= len(lista[i])
    if a>2 and lista[i][0]== lista[i][a-1]:
        count = count +1
print (count)
'''
###ejercicio5
'''
n=int(input("tam list que desea ingresar"))
lista=[]
for i in range(n):
    a=int(input("ingrese list[%d]="%(i)))
    lista = lista + [a]
    print(lista)

for j in range(n//2):
    a=lista[2*j]
    b=lista[(2*j)+1]
    lista[2*j] = b
    lista[(2*j)+1]=a
print (lista)
'''

###ejercicio6
'''
lista=[7,2,5,4,3,6,1]
count=0
for i in range(len(lista)):
    if lista[i]> lista[i-1] and lista[i]> lista[i+1]:
        count = count +1
print(count)
'''

#ERATOSTENES
n=int(input('ingrese n:'))
lista=[1]*n
lista[0]=0
for i in range(1,n):
    count=0
    for j in range(1,i):
        if i%j==0:
            count+=1
    if count!=2:
        lista[i]=0
print(lista)
    
    
    
    
    
    
    
    
    
    
    