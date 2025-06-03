n,m = map(int,input().split())
a = list(map(int,input().split()))
ans = 0
for i in range(n):
    ans += a[i]
a.sort()
if a[n-m]/ans < 1 / (4 * m):
    print('No')
else:
    print('Yes')
