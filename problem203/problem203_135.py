import math
A, B = map(int, input().split())

AA = A * 100 / 8
BB = B * 100 / 10

L = []
for i in range(10000):
    if math.floor(i * 0.08) == A and math.floor(i * 0.1) == B:
        L.append(i)
    
L = sorted(L)
if L == []:
    print(-1)
    exit()

print(L[0])