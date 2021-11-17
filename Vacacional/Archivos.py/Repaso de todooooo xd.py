#Ejercicios en clases 1
#1.-Pedir una nota y calculo el porcentaje de dicha nota
'''
x=int(input("Calificacion: "))
if (x<0) or (x>10):
    print("Inserte numero de 1 al 10")
else:
    y=(x*3.5)
    print("El porcentaje es",y,"%")
'''
#2.Escribir si el numero es positivo o no
'''
x=int(input("Inserte numero: "))
if x<0:
    print(x,"es negativo")
else:
    print(x,"es positivo")
'''
#3.Escriba año actual y año cualquiera, escribir cuantos años faltan o han pasado
'''
x=int(input("Año actual: "))
y=int(input("Año x: "))
z=x-y
if z>0:
    print("Han pasado",z,"años")
else:
    print("Faltan",z,"años")
'''
#6 y 7.
'''
x=int(input("Numero1: "))
y=int(input("Numero2: "))
z=x/y
if x==0 or y==0:
    print("No se puede divivdir para 0")
if z%1==0:
    print("Es entera")
else:
    print("No es")
'''
#8.Programa que vea cual numero es mayor o menor o si son iguales
'''
x=int(input("Numero1: "))
y=int(input("Numero2: "))
if x>y:
    print(x,"es mayor y",y,"es menor")
if x<y:
    print(y,"es mayor y",x,"es menor")
if x==y:
    print("son iguales")
'''
#9.Ver si es par o impar
'''
x=int(input("Número: "))
if x%2==0:
    print("Es par")
else:
    print("Es impar")
'''
#10.Verificar si es multiplo de 3
x=int(input("Número: "))
if x%3==0:
    print(x,"es múltiplo de 3")
else:
    print("no es multiplo")

    


