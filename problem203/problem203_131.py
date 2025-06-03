import math
A, B = map(int, input().split())
r = -1
for i in range(1, 1111):
    if A == math.floor(i*0.08) and B == math.floor(i*0.10):
        r = i
        break

print(r)
