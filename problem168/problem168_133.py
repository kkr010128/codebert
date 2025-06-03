n,m = map(int,input().split())
a = [int(s) for s in input().split()]
daycount = 0
for i in range(m):
    daycount += a[i]
if n - daycount >= 0:
    print(n - daycount)
else:
    print(-1)