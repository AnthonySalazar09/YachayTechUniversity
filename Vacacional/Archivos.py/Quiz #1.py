#1
'''
x=int(input("inserte un número"))
count=1
for i in range(1,x+1):
    count*=i
print(count)
'''
#2
'''
x=int(input("inserte número: "))
for i in range(x):
    if (i%3==0) or (i%5==0):
        print(i,"es divisible")
    else:
        print(i,"no es divisible")
'''
#3
x=int(input("ingrese velocidad= "))
suspendidos= (x-70)//5
if x<70:
    print("ok")
else:
    if suspendidos <=12:
        print("puntos suspendidos", suspendidos)
    else:
        print("licencia suspendida")
        
        
