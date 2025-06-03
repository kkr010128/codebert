n = int(input())
M = int(n**(0.5))
ans = [0]*(n+1)
for x in range(1,M+1):
    for y in range(1,10**2):
        for z in range(1,10**2):
            if x**2+y**2+z**2+x*y+y*z+z*x > n:
                break
            ans[x**2+y**2+z**2+x*y+y*z+z*x] += 1
        if x**2+y**2 > n:
            break
for i in range(n):
    print(ans[i+1])