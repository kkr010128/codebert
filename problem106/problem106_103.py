n = int(input())
ans = [0]*(n+1)
for x in range(1, 100):
    for y in range(1, 100):
        for z in range(1, 100):
            k = x**2+y**2+z**2+x*y+y*z+z*x
            if k<=n: ans[k]+=1
for i in range(1, n+1):
    print(ans[i])
