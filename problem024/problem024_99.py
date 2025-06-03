def ok(a, n, k, p):
    t = 0
    t_cnt = 0
    for w in a:
        if p < w:
            return -1
        if t + w > p:
            t_cnt += 1
            if t_cnt >= k:
                return -1
            t = w
        else:
            t += w
    return 0


n, k = map(int, input().split())
a = [int(input()) for _ in range(n)]

P_max = n * 10000 // k + 10001

l = 0
r = P_max
m = 0
while l < r - 1:
    m = (l + r) // 2
    if ok(a, n, k, m) == 0:
        r = m
    else:
        l = m

print(r)








