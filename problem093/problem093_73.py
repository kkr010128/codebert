n, k = (int(x) for x in input().split())
P = list(int(x) - 1 for x in input().split())
C = list(int(x) for x in input().split())

ans = -1e18
for si in range(n):
    S = [C[si]]
    x = P[si]
    while x != si:
        S.append(S[-1] + C[x])
        x = P[x]
    m = len(S)
    if k <= m:
        tmp = max(S[:k])
    else:
        loop = k // m
        r = k % m
        tmp = max(S[-1] * (loop - 1) + max(S), max(S))
        if r != 0:
            tmp = max(tmp, S[-1] * loop + max(S[:r]))
    ans = max(ans, tmp)
print(ans)