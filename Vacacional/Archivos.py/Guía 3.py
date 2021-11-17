#Guía 3
#7.
'''
lista=["Di","buen","día","a","papa"]
print(lista)

def al_revez(x):
    y=[]
    for i in range(len(x)):
        y.append(x[-i-1])
     
                    
    return y

print(al_revez(lista))
'''
#8.                         
'''            
lista=[1,1,1,3,4,1,1,3,3]

def f(lista1):
    lista3=[]
    count=1
    for i in range(len(lista1)-1):
        if lista1[i]==lista1[i+1]:
            count+=1
        else:
            lista3.append((lista1[i],count))
            count=1
        if i==(len(lista1)-2):
            lista3.append((lista1[i+1],count))
            
            
    return lista3

print(f(lista))            
'''
#9.
'''
def maxi(x):
    m=x[0]
    for i in range(len(x)):
        if m<x[i]+i:
            m=x[i]+i
    return m
lista=[1,3,5,3,2,1,5]
print(maxi(lista))
'''
            
            
            


