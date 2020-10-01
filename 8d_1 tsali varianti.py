import sympy as sp
import numpy as np
import cmath
from sympy.solvers import solve
from sympy import Symbol
if (2>3) or (3<4):
    print ('a')
a=np.zeros( (8, 8))
#print(a)
#A[1][2]=3
#print(A)
def chasma(i,j):
    global a
    a[i][j]=9
    i1=i
    j1=j
    while (i1>0) and (j1>0):
        i1=i1-1
        j1=j1-1
        if a[i1][j1]==0:
            a[i1][j1]=i+1
    i1=i
    j1=j
    while (i1<7) and (j1>0):
        i1=i1+1
        j1=j1-1
        if a[i1][j1]==0:
            a[i1][j1]=i+1
    i1=i
    j1=j
    while (i1<7) and (j1<7):
        i1=i1+1
        j1=j1+1
        if a[i1][j1]==0:
            a[i1][j1]=i+1
    i1=i
    j1=j
    while (i1>0) and (j1<7):
        i1=i1-1
        j1=j1+1
        if a[i1][j1]==0:
            a[i1][j1]=i+1
    i1=i
    j1=j
    for j1 in range(0,8):
        if a[i1][j1]==0:
            a[i1][j1]=i+1
    j1=j
    for i1 in range (0,8):
        if a[i1][j1]==0:
            a[i1][j1]=i+1
#print(a)
def amogdeba(i,j):
    global a
    a[i][j]=0
    i1=i
    j1=j
    while(i1>0) and(j1>0):
        i1=i1-1
        j1=j1-1
        if a[i1][j1]==i+1:
            a[i1][j1]=0
    i1=i
    j1=j
    while (i1<7) and (j1>0):
        i1=i1+1
        j1=j1-1
        if a[i1][j1]==i+1:
            a[i1][j1]=0
    i1=i
    j1=j
    while (i1<7) and(j1<7):
        i1=i1+1
        j1=j1+1
        if a[i1][j1]==i+1:
            a[i1][j1]=0
    i1=i
    j1=j
    while (i1>0) and (j1<7):
        i1=i1-1
        j1=j1+1
        if a[i1][j1]==i+1:
            a[i1][j1]=0
    i1=i
    j1=j
    for j1 in range (0, 8):
        if a[i1][j1]==i+1:
            a[i1][j1]=0
    for i1 in range (0,8):
        if a[i1][j]==i+1:
            a[i1][j]=0
#print (a)
k=0
i=0
j=0
s=0
while s!=8:
    if a[i][j]!=0:
        j=j+1
        print(j)
    else:
        chasma(i,j)
        s=s+1
        j=1
        i=i+1
        print(a)
    if j==8:
        if s==8:
            print (a)
        else:
            i=i-1
            for j1 in range (0,8):
                if a[i][j1]==9:
                    amogdeba(i,j1)
                    s=s-1
                    break
            if j1<7:
                j=j1+1
            else:
                i=i-1
                for j1 in range (0,8):
                    if a[i][j1]==9:
                        amogdeba(i,j1)
                        s=s-1
                        break
                j=j1+1
                
        
    
    
        
    
        
    
