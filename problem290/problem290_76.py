n, k = map(int, input().split())
a = map(int, input().split())
f = map(int, input().split())
a = sorted(a)
f = sorted(f)[::-1]


def c(x):
    # x決めると必要な修行回数も決まる
    res = 0
    for O, K in zip(a, f):
        d = max(0, O * K - x)
        res += (d + K - 1) // K
    return res <= k


l = -1
r = 1 << 60
while r - l > 1:
    mid = (l + r) >> 1
    if c(mid):
        r = mid
    else:
        l = mid
print(r)
