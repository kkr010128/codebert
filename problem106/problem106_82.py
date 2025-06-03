import math
n = int(input())
t = [0] * (n + 1)
m = math.floor(math.sqrt(n))

for i in range(1,m):
    for j in range(1,m):
        for k in range(1,m):
            p = i*i+j*j+k*k+i*j+j*k+i*k
            if p <= n:
                t[p] += 1

for i in range(1,n + 1):
    print(t[i])