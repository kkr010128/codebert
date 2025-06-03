n, k = map(int, input().split())
W = [int(input()) for _ in range(n)]
def can_load(W, k, q, n):
    i = 0
    for _ in range(k):
        s = 0
        while i < n and s + W[i] <= q:
            s += W[i]
            i += 1
    if i == n:
        return True
    else:
        return False

# 積載量をmidと仮定して二分探索
hi = 10 ** 9  # OK
lo = 0  # NG
while hi - lo > 1:
    mid = (hi + lo) // 2
    if can_load(W, k, mid, n):
        hi = mid
    else:
        lo = mid
print(hi)
