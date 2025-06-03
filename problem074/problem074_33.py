n, k = map(int, input().split()); m = 998244353; a = []
for i in range(k): a.append(list(map(int, input().split())))
b = [0]*n; b.append(1); c = [0]*n; c.append(1)
for i in range(1, n):
    d = 0
    for j in range(k): d = (d+c[n+i-a[j][0]]-c[n+i-a[j][1]-1])%m
    b.append(d); c.append(c[-1]+d)
print(b[-1]%m)