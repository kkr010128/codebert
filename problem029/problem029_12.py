import math
l=input().split()
x1=float(l[0])
y1=float(l[1])
x2=float(l[2])
y2=float(l[3])

A=math.sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2))
print(A)
