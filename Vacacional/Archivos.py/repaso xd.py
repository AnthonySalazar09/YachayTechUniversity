#|
'''
x=int(input("Cantidad de números: "))
a=[]

for i in range(x):
    y=int(input("Números: "))
    a.append(y)
print(a)
count=0
for i in range(len(a)):
    if a[i]==1:
        count+=i
print(count)
'''
#2.

x=input("palabra: ")
palindromo = 1
for i in range(len(x)//2):
    if x[i]!=x[-i-1]:
        palindromo = 0
        break
print(palindromo)

