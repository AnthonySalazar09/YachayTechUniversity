# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 17:15:28 2019

@author: COMPUTRONICA
"""

import math
a=(float(input("ingrese valor de a = ")))
b=(float(input("ingrese valor de b = ")))
c=(float(input("ingrese valor de c = ")))
det=(b**2-4*a*c)
if (det>0):
 x=(-b+math.sqrt(det))/(2*a)
 x2=((-b-math.sqrt(det))/2*a)
 print("x = " + str(x),"x2 = " + str(x2))
elif(det<0):
    xentero=(-b/2*a)
    x2entero=(-b/2*a)
    ximg=(+math.sqrt(-det)/2*a)
    x2img=(-math.sqrt(-det)/2*a)
    print("parte entera de x = " + str(xentero))
    print("parte entera de x2 = " + str(x2entero))
    print("parte imaginaria de x = " + str(ximg))
    print("parte imaginaria de x2 = " + str(x2img))
else:
    x3=(-b/2*a)
    print("x = " + str(x3)) 



    
    
    