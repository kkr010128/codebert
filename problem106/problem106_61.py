n = int(input())
ans = [0]*(n+1)
r = range(1, int(n**0.5)+1)
for x in r:
    for y in r:
        for z in r:
            a = x**2 + y**2 + z**2 + x*y + y*z + z*x
            if a<=n:
                ans[a] += 1
for i in ans[1:]:
    print(i)