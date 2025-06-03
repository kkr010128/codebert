N, K = map(int, input().split())
R, S, P = map(int, input().split())
POINTS = (R, P, S)
T = [("r", "p", "s").index(c) for c in input()]
WIN = [(t + 1) % 3 for t in T]

ans = 0
for i in range(K):
    p = [0] * 3
    p[WIN[i]] = POINTS[WIN[i]]
    j = i + K
    while j < N:
        n = [-1] * 3
        for px, pp in enumerate(p):
            if pp < 0:
                continue
            for nx in range(3):
                if nx == px:
                    continue
                np = pp
                if nx == WIN[j]:
                    np += POINTS[WIN[j]]
                n[nx] = max(n[nx], np)
        p = n
        j += K
    ans += max(p)
print(ans)