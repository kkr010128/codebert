import math
 
A, B, N = map(int, input().split())
 
x = 0
if N < B:
    x = N
else:
    x = B - 1
 
print(math.floor(A * x / B) - A * math.floor(x / B))