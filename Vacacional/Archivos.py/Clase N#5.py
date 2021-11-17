#1
'''
Lista=[1,2,8]
A=[Lista,8,"holha",9]
print(A[0][0])
'''
#2
'''
A=["pan","huevos",100,1234]
print(A[0])
print(A[3])
'''
#3. Recorrer una lista
'''
Lista=[1,2,8]
A=[Lista,8,"holha",9]
i=0,1,2,3
for i in range(len(A)):
    print(A[i])
for i in A:
    print(i)
'''
#4 Cambiar elementos de una lista
'''
Lista=[1,2,8]
A=[Lista,8,"holha",9]
A[0]=0
print(A)
'''
#5. Agregar elemento a una lista
'''
Lista=[1,2,8]
A=[Lista,8,"holha",9]
A=A+[0]
A.append(5)
print(A)
'''
#6.Crear una lista
'''
x=int(input("ingrese tamaño de la lista: "))
lista=[]
for i in range(x):
    y=int(input("ingrese número: "))
    lista=lista+[y]
print(lista)
'''
#7.
'''
A=[86,86,85,85,85,83,23,45,84,1,2,0,87]
mayor=A[0]
menor=A[0]
for i in range(len(A)):
    if A[i]>mayor:
        mayor=A[i]
    if A[i]<menor:
        menor=A[i]
    
print(mayor)
print(menor)
'''
#8.
'''
A=[86,86,85,85,85,83,23,45,84,1,2,0,87]
mayor=A[0]
index=0
for i in range(len(A)):
    if A[i]>mayor:
        mayor=A[i]
        print("mayor=",mayor,"indice=",i)
        index=i
print(mayor)
print(index)
'''
#9.Sumar la lista

A=[86,86,85,85,85,83,23,45,84,1,2,0,87]
count=0
for i in range(len(A)):
    count=count+A[i]
print(count)
        
