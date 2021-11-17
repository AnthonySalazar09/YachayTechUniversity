'''
for i in range(0,5,2):
        print(i)
'''

'''
x="yachay"
count=int(0)
for i in x:
    if i=="a":
        count=count+1
    elif i=="e":
        count=count+1
    elif i=="i":   
        count=count+1
    elif i=="o":
        count=count+1
    elif i=="u":
        count=count+1
print(count)
'''
#Escribir un programa que haga una tabla de multiplicar
'''
x=int(input("cualquier número"))
for i in range(1,11):
      print(x,'x',i,'=',x*i)
'''
#Escribir los nùmero enteros y a la derecha debe salir si es par o impar:
'''
x=int(input("número: "))

for i in range(0,x+1):
    if i%2==0:
     print(i,"par")
    else:
     print(i,"inpar")
'''
#Crear 
'''
n=int(input("ingrese"))
for i in range(1,n):
      print('*'*i)
'''
#Arbol de navidad
'''
n=int(input("ingrese cualquier dato"))
z=(n//2)

for i in range(1,n+1,2):
      print(z*" "+i*'*')
      z-=1
'''

#
'''
x=input("Ingrese su nombre: ")
y=input("Ingrese su nacionalidad: ")
if y!="Ecuatoriano":
    print("Ingrese su número de pasaporte")
else:
    print("Ingrese su número de cédula")
z=input(":")
print("Bienvenido",x,"de nacionalidad",y,)
'''
#
x=str(input("Ingrese palabara: "))
y=str(input("Ingrese palabra: "))
lista1=list(x)
lista2=list(y)
count=0
count2=0
for i in range(len(lista1)):
    if lista1[i]==x:
        count+=1
        for j in range(len(lista2)):
            if lista2[j]==y:
                count2+=1
            if count>count2:
                print(x)
               

      

      
      

    
         
         
      
      
      
      
      
      
        
        
    
