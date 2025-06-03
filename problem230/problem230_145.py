n, d, a = map(int, input().split())
xh = []
for _ in range(n):
    x, h = map(int, input().split())
    xh.append((x, h))

xh.sort(key=lambda x:x[0])

def bisect(x):
    ok = n
    ng = -1
    while abs(ok-ng)>1:
        mid = (ok+ng)//2
        if xh[mid][0]>x:
            ok = mid
        else:
            ng = mid
    return ok

out = [0]*(n+1)
ans = 0
accu = 0
for ind, (x, h) in enumerate(xh):
    accu -= out[ind]
    h -= accu
    if h<=0:
        continue
    ans += (h+a-1)//a
    accu += ((h+a-1)//a)*a
    out[bisect(x+2*d)] += ((h+a-1)//a)*a
print(ans)