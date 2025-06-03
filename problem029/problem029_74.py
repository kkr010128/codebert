import math
L=list(map(float,input().split()))
A=(L[0]-L[2])*(L[0]-L[2])
B=(L[1]-L[3])*(L[1]-L[3])
V=math.sqrt(A+B)
print(round(V,8))
