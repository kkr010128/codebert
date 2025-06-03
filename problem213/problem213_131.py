n = int(input())
x = list(map(int,input().split()))
x.sort()

xmin = x[0]
xmax = x[-1]
ans = 10**9
for i in range(xmin, xmax+1):
    d = 0
    for j in x:
        d += (j - i)**2
    ans = min(ans, d)
print(ans)