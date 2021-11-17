#1.Crear un programa que en base al menú local comercial
'''
precios=[0.0,3.50,2.50,4.00,3.50,1.75,1.50,2.25,3.75,1.25]
count=0
while True:
    y=int(input("Ingrese orden: "))
    if y==0:
        break
    if y>0:
      count+=precios[y]
print("el total es",count)
'''
#2.Programa que reliaze la transcrpción genética de ADN a ARN.

A=["G","C","T","A"]
B=["C","G","A","U"]
x="CTAG"
for i in x:
    for j in range(len(A)):
        if i==A[j]:
         print(B[j],end='')

#3.
'''
count=0
for i in range(5):
    for j in range(3):
       count+=1 
       print("hola")
'''
#Práctica N6:
#1.
'''
n = input("ingrese numero de cedula")
lista = list(n)
print(lista)
for i in range(len(lista)):
    lista[i]= int(lista[i])
print (lista)
x= lista[len(lista)-1]
print(x, end=" ")
print(x)
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
#2.

'''
lista=[5,10,2,3,1,8,11,15,9,13]
count1=0
count2=0
for i in range(len(lista)):
          if lista[i]%2==0:
           count1+=1
          else:
           count2+=1
print(count1,"pares")
print(count2,"inpares")
'''
#3
'''
x=int(input("tamaño de lista: "))
lista=[]
for i in range(x):
    y=int(input("números: "))
    lista.append(y)
mini=lista[0]
maxi=lista[0]
for i in range(len(lista)):
    if lista[i]<mini:
        mini=lista[i]
    if lista[i]>maxi:
        maxi=lista[i]
print(maxi-mini)
'''
#4.
'''
a=["abc","xyz","aba","1221"]
count=0
for i in range(len(a)):
    if len(a[i])>=2 and a[i][0]==a[i][-1]:
        count+=1
print(count)
'''
#5.
'''
A=[1,2,3,4,5,6]
for i in range(0,len(A),2):
    Aux=A[i]
    A[i]=A[i+1]
    A[i+1]=Aux
print(A)
'''
#6.
'''
a=[1,5,1,5,1]
count=0
for i in range(len(a)):
    if a[i]>a[i-1] and a[i]>a[i+1]:
        count=count+1
print(count)
'''
    
    
    





        

        
    
