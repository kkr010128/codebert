n,k = map(int, input().split())

A = list(map(int,input().split()))
F = list(map(int,input().split()))

A.sort()
F.sort(reverse=True)

def is_ok(x):
    c = 0
    for a, f in zip(A, F):
        c += max(0, a-x//f)
    if c <= k:
        return True
    else:
        return False

ng = -1
ok = 10**18
while ng+1 < ok:
    c = (ng+ok)//2
    if is_ok(c):
        ok = c
    else:
        ng = c
print(ok)
