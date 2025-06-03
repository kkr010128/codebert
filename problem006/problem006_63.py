import math
res = 100
N = int(input())
for i in range(N):
    res = math.ceil(res * 1.05)
print("%d000" % res)

