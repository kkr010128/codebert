import math
A,B,N = map(int,input().split())
if N >= B:
    N = B - 1
print(math.floor(A*N/B) - A * math.floor(N/B))