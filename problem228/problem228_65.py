import math
H=int(input())
j=1
t=1
while H!=1:
    H=math.floor(H/2)
    t*=2
    j+=t
print(j)