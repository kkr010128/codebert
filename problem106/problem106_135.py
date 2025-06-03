import math
N = int(input())
ans = [0]*(N+1)
Nruto = math.sqrt(N)
Nruto = math.floor(Nruto)+1
for x in range(1, Nruto):
    for y in range(1, Nruto):
        for z in range(1, Nruto):
            n = x**2+y**2+z**2+x*y+y*z+z*x
            if n <= N:
                ans[n] += 1
for i in range(1, N+1):
    print(ans[i])
