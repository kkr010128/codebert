def f(p, k, W):
    i = 0
    t = 0
    s = 0
    while i < len(W) and t < k:
        if s + W[i] <= p:
            s += W[i]
            i += 1
        else:
            s = 0
            t += 1
    return i


n, k = map(int, input().split())
W = [int(input()) for _ in range(n)]

l = 0
r = 100000 * 10000 // k
while r - l > 1:
    mid = (l + r) // 2
    v = f(mid, k, W)
    if v >= n:
        r = mid
    else:
        l = mid

print(r)

