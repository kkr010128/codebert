N = int(input())
ans = [0]*(1+N)

for x in range(1, 10**2+1):
    for y in range(1, 10**2+1):
        for z in range(1, 10**2+1):
            v = x*x+y*y+z*z+x*y+y*z+z*x
            
            if v<=N:
                ans[v] += 1

for i in range(1, N+1):
    print(ans[i])