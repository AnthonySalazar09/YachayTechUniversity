#
'''
def factorial(n):
    if n==1 or n==0:
        return 1
    else:
        return(n*factorial(n-1))
x=int(input("Factorial de: "))
print("El resultado es",factorial(x))
'''
#
'''
def exponencial(a,n):
    if n==0:
        return(1)
    else:
        return(a*exponencial(a,n-1))
x=int(input("Número de : "))
y=int(input("Elevado a la : "))
print("Queda",exponencial(x,y))
'''
'''
#Ejercicio de la guia
lista1=['a','b','c','d','e','f','g','h','i','j','k','x','y','z']
x=str(input("ingrese: "))
y=''
for i in x:
    for j in range(len(lista1)):
        if i==lista1[j]:
            y+=lista1[j-3]
print(y)
'''
#
def fibonacci(n):
    if n==1 or n==2:
        return 1
    else:
        return(fibonacci(n-1)+fibonacci(n-2))
x=int(input("Número: "))
print("Resultado",fibonacci(x))


    
