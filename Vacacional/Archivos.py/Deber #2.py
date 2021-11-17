#Ejercicio 1:
'''
x=int(input("inserte un número: "))
y=int(input("inserte otro número: "))
z=int(input("inserte último número: "))
if x==y and y==z and x==z:
    print("Todos son iguales")
elif x==y:
    print("Solo",x,"y",y,"son iguales")
else:
    print("ninguno son iguales")
'''
#Ejercicio 2:

a=float(input("coeficiente a: "))
b=float(input("coeficiente b: "))
c=float(input("coeficiente c: "))

d=(b**2)-(4*a*c)
if a==0 and b==0 and c==0:
    print("Todas son soluciones")
if d<0:
    print("no tiene solución")

elif d==0:
    x=((-b+(d**(0.5)))/(2*a))
    print("tiene una sola solución",x,)
else:
    x1=((-b+(d**(0.5)))/(2*a))
    x2=((-b-(d**(0.5)))/(2*a))
    print("esta ecuación tiene dos soluciones, son:",x1,"o",x2,)
    
    
