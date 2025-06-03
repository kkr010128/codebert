r, c = map(int, input().split())
a = [0]*(c+1)
for _ in range(r):
    v = list(map(int, input().split()))
    s = 0
    for i, e in enumerate(v):
        s+=e
        a[i]+=e
    v.append(s)
    print(*v)
    a[-1]+=s
print(*a)