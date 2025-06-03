import math
A,B,H,M = map(int,input().split())
t1 = (30*H+M/2)*math.pi/180
x1 = A*math.cos(t1)
y1 = A*math.sin(t1)
t2 = M*math.pi/30
x2 = B*math.cos(t2)
y2 = B*math.sin(t2)
d = ((x1-x2)**2+(y1-y2)**2)**0.5
print(d)