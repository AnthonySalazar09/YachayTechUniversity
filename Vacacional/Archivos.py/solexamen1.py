# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 17:00:55 2020

@author: hp
"""

#examen1
#1.- Escriba un programa que tome una lista de valores enteros. El
#programa debe de realizar la suma de todos los índices que
#representen la posición del valor 1 en la lista.

x= int(input('ingrese tamaño de lista:'))
a=[]
for i in range(x):
    y=int(input('ingrese elemento='))
    a.append(y)
count=0
for i in range(len(a)):
    if a[i]==-1:
       count+=i
print(i)       

#2.- Escribra un programa que permita verificar si una palabra
#ingresada por el usuario es un palíndromo. Un palíndromo es una
#palabra o frase que de izquierda a derecha o de derecha a izquierda
#se lee igual. Ejemplos en Inglés: madam, level, racecar. Ejemplos
#en Español: oro, oso, somos, sometemos. Mostrar un mensaje al
#final de que si es palíndromo o no
'''
x=input('ingrese palabra:')
y=''
for i in range(1,len(x)+1):
    y= y + x[-i]
if x==y:
    print('es palindromo')
else:
    print('no es palindromo')
''' 
#3.- Escriba un programa que tome una lista S de strings de tamaño
#N. La función debe encontrar el primer carácter de cada elemento
#de la lista S que ocurre solo una vez. La salida debe ser una nueva
#lista de tamaño N, con los caracteres encontrados, si no existe
#dicho carácter agregar -1 a la nueva lista.
'''
x= int(input('ingrese tamaño de lista:'))
a=[]
for i in range(x):
    y=input('ingrese elemento=')
    a.append(y)
p=[]
for i in range(len(a)):
    count=0
    for j in range(1,len(a[i])):
        if a[i][0]==a[i][j]:
            count+=1
    if count==0:
        p.append(a[i][0])
    else:
        p.append('-1')
print(p)            
'''         
            
            
