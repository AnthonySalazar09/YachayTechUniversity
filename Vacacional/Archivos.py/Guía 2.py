#Guía 2
#1.Calcular si el triángulo es isósceles,equiláteri o escaleno
'''
x=int(input("inserte numero: "))
y=int(input("inserte numero: "))
z=int(input("inserte numero: "))
if x==y and y==z:
    print("Es un equilátero")
elif x==y or y==z or x==z:
    print("isosceles")
else:
    print("escaleno")
'''
#2.Programa paa transofrmar  de cm a km m y a cm
'''
c=int(input("Distancia en cm: "))
if c<=0:
    print("Escriba una distancia mayor a 0")
else:
    cm=c%100
    aux=c//100
    m=aux%1000
    km=aux//1000
    
print(c,"centímetro son",km,"km",m,"m",cm,"cm")
'''
#3.Programa que muestre elementos comunes entre dos listas
'''
a=[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c=[]
for i in a:
    for j in b:
        if i==j:
            enc = False
            for k in c:
                if k==i:
                    enc=True
                    break
            if not enc:
                c.append(i)
print(c)
'''
'''
a=[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c=[]
for i in a:
    for j in b:
        if i==j and i not in c:
            c.append(i)
print(c)
'''

#4.Programa que tome una lista´e imprima los numeros del rango de 5 a 10
'''
a=[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for i in a:
    if 5<=i<=10:
        print(i)
'''
#5.Progrma que una dos listas
'''
a=[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
for i in b:
    a.append(i)
print(a)
'''
#6.Programa que tome dos listas y ponga si son V o F si la menor esta en la mayor 
'''
a=[1,2,3,4,5,6,7,8,9]
b=[2,3,10]
iguales = True
for i in range(len(a)- len(b)+1):
    iguales = True
    for j in range(len(b)):
        if a[i+j]!=b[j]:
            iguales = False
            break
    if iguales:
        break
        
if iguales:
    print("si")
else:
    print("no")
'''
'''
a=[1,2,3,4,5,6,7,8,9]
b=[2,3,4]
c=False
for i in range(len(a)-len(b)):
    count=0
    for j in range(len(b)):
        if a[i+j]==b[j]:
                   count+=1
        if count==len(b):
            c=True
print("si")
 '''                
#7.Programa que diga cuantas veces esta el numero en la lista
"""
b = int(input("número: "))
a=[1,2,1,3,3,3,4,5,6,7,8,9]
acu = 0
for i in a:
    acu+= int(i==b)
print(acu)
"""
#8.Programa que transfrome en -1 uno cada número par
"""
a=[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for i in range(len(a)):
    if a[i]%2==0:
        a[i]=-1
print(a)
"""
#9.Programa que tome cada número impar y la transforme en -1
"""
a=[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for i in range(len(a)):
    if a[i]%2!=0:
        a[i]=-1
print(a)
"""
#10.Programa que transforme cada elemento primo en -1

a=[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
print(a)
for j in range(len(a)):
    if a[j]!=1:
        primo=True
        for i in range(2,a[j]):
            if a[j]%i==0:
                primo = False
                break
        if primo:
            a[j]=-1
print(a)

#Como saber si es número factorial?
'''
a=[1,2,3,4,5,24,76,6,7,8,9]
Fact=[]
maxi=a[0]
for i in a:
    if i>maxi:
        maxi=i
print(maxi)
i=1
count=1
while True:
    count*=i
    if count>maxi:
        break
    else:
        Fact.append(count)
        i+=1
print(Fact)
for i in a:
    if i in Fact:
        print(i)
'''

'''
c=90001
segundos=c%60
aux=c//60
minutis=aux%60
horas=((c//60)//60)%24
dias=((c//60)//60)//24
print(c,"segundos",dias,"dias",horas,"horas",minutis,"minutos",segundos,"segundos")
'''
