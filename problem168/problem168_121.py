n,m = map(int,input().split())
a = list(map(int,input().split()))
ans = 0
for i in range(m):
    ans += a[i]
if n < ans:
    print(-1)
else:
    print(n-ans)