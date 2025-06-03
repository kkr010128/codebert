import math

lrd=input().split()
l=int(lrd[0])
r=int(lrd[1])
d=int(lrd[2])
a=math.ceil(l/d)
b=math.floor(r/d)
print(b-a+1)

