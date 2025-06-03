n = int(input())
x = list(map(int,input().split()))
x.sort()
ans = 10 ** 8
for p in range(x[0],x[-1]+1):
    m = 0
    z = 0
    for i in range(n):
        z = x[i] - p
        m += (z ** 2)
    ans = min(ans,m)
print(ans)