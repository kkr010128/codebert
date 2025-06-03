import math
N = int(input())
ans = [0]*(N+1)
owari = math.sqrt(N)
owari = math.ceil(owari)
for x in range(1, owari):
    a = x*x
    for y in range(1, owari):
        b = y*y
        c = x*y
        for z in range(1, owari):
            hantei = z*(z+x+y)+a+b+c
            if hantei > N:
                break
            ans[hantei] += 1

for i in range(1, N+1):
    print(ans[i])
