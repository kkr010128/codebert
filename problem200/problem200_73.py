A, B, m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
minp = min(a) + min(b)
for i in range(m):
    x, y, c = map(int,input().split())
    minp = min(minp, a[x-1] + b[y-1] -c)
print(minp)