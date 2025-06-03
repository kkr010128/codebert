n, k = map(int, input().split())
aa = list(map(int, input().split()))
ff = list(map(int, input().split()))

a = sorted(aa, reverse=True)
f = sorted(ff)

def C(x):
    ret = 0
    for i in range(n):
        ret += max(0, a[i] - x // f[i])
    return ret

lb = -1
ub = 10 ** 12 + 1
while (ub - lb) > 1:
    mid = (ub + lb) // 2

    if C(mid) > k:
        lb = mid
    else:
        ub = mid
print(ub)
