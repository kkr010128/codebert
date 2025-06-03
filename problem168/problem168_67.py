n,m = map(int,input().split())
alist = list(map(int,input().split()))

d = n - sum(alist)
if d < 0:
    print(-1)
else:
    print(d)