n, k = map(int, input().split())
a = list(map(int, input().split()))
f = list(map(int, input().split()))
a.sort()
f.sort(reverse=True)

def solve(x):
    lk = k
    for i, j in zip(a, f):
        if i*j<=x:
            continue
        lk -= (j*(i+1)-x-1)//j
        if lk<0:
            return False
    return True

ok = 10**12
ng = -1
while abs(ok-ng)>1:
    mid = (ok+ng)//2
    if solve(mid):
        ok = mid
    else:
        ng = mid

print(ok)
