import math
N = int(input())
ans = [0]*(N+1)
Nruto = math.floor(math.sqrt(N))
for x in range(1, Nruto):
    a = x**2
    for y in range(1, Nruto):
        b = y**2
        c = x*y
        for z in range(1, Nruto):
            keisan = a+b+c+z*(z+y+x)
            if keisan > N:
                break
            ans[keisan] += 1
for i in range(1, N+1):
    print(ans[i])
