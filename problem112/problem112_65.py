def solve():
    P.sort(reverse = True)
    M.sort()
    P.append(-1)
    M.append(1) # add endpoint
    p, m = [], []
    while len(p) + len(m) < k:
        if P[len(p)] < -M[len(m)]:
            m.append(M[len(m)])
        else:
            p.append(P[len(p)])
    if len(m)%2 == 0: return p + m

    exist_p = len(p) > 0
    exist_m = len(m) > 0
    remain_P = len(P) - 1 > len(p)
    remain_M = len(M) - 1 > len(m)
    if exist_p & remain_M & exist_m & remain_P:
        if abs(p[-1] * P[len(p)]) < abs(m[-1] * M[len(m)]):
            p.pop()
            m.append(M[len(m)])
        else:
            m.pop()
            p.append(P[len(p)])
    elif exist_p & remain_M:
        p.pop()
        m.append(M[len(m)])
    elif exist_m & remain_P:
        m.pop()
        p.append(P[len(p)])
    else:
        M.pop() # del endpoint
        m = sorted(M, reverse = True)[:k]
    return p + m

n, k = map(int, input().split())
P, M = [], [] # plus, minus
for a in map(int, input().split()):
    if a < 0: M.append(a)
    else: P.append(a)
ans, MOD = 1, 10**9 + 7
for a in solve(): ans *= a; ans %= MOD
ans += MOD; ans %= MOD
print(ans)
