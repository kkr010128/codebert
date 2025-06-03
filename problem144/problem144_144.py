import math
A, B, H, M = map(int, input().split())
H = math.radians((H*60 + M)/2)
M = math.radians(M*6)

Ax = A*math.cos(H)
Ay = A*math.sin(H)
Bx = B*math.cos(M)
By = B*math.sin(M)

l = math.sqrt((Ax - Bx)**2 + (Ay - By)**2)
print(l)