#Guía 2.0
#26.

def crearmatriz(n,m):
    c=[]
    for i in range(n):
        c.append([0]*m)
    for i in range(len(c)):
        for j in range(len(c[i])):
            c[i][j]=int(input("Elemento [%d][%d]]"%(i,j)))
    return c

a=crearmatriz(3,3)
b=crearmatriz(1,3)

print(a)
print(b)

for i in range(len(a)):
    count=0
    for j in range(len(a[i])):
        if a[i][j]==b[0][j]:
            count+=1
    if count==len(b[0]):
        print("fila %d es igual a la b"%(i))

#27.
'''
def buscarfila(a,b):
    x=False
    for i in range(len(a)):
        if a[i]==b:
            x=True
    return x

print(buscarfila(a,b))
'''
#28
'''
def buscarcolum(a,b):
    x=False
    for j in range(len(b)):
        count=0
        for i in range(len(a)):
            if a[j][i]==b[i][0]:
                count+=1
        if count==len(b):
            x=True
    return x


a=crearmatriz(3,3)
b=crearmatriz(3,1)
print(a)
print(b)
print(buscarcolum(a,b))
'''
#31.
'''
c=[[1,2],[3,4]]
d=[[1,2],[4,5]]
def sumarSoloPares(a,b):
    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i][j]%2==0:
                a[i][j]=a[i][j]+b[i][j]
            else:
                a[i][j]=0
    return a
print(sumarSoloPares(c,d))
'''
#32.
'''
def sumarlimitado(a,b):
    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i][j]+b[i][j]<10:
                a[i][j]=a[i][j]+b[i][j]
            else:
                a[i][j]=0
    return a
'''
#33.
'''
def contarrepeticiones(A,x):
    count=0
    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i][j]=x
            count+=
'''
#34.
'''
def intercambiarfilas (a,k,i):
    for i in range(len(a[0])):
        aux=a[k][i[
        a[k][i]=a[l][i]
        a[l][i]=aux
    return a
'''
        
        
