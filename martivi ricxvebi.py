import math
n=1000
print (1,",",2,end=", ")
for j in range (3, n):
    s=0
    b=j
    sq=math.sqrt(j)
    sq1=int(round(sq))
    for i in range (2, (sq1+1)):
        if j%i==0:
           s=1
    if s==0:
        print(b,end=", ")
