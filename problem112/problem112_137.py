def solve():
    can_positive = False
    if len(P) > 0:
        if k < n: can_positive = True
        else: can_positive = len(M)%2 == 0
    else: can_positive = k%2 == 0

    if not can_positive: return sorted(P+M, key=lambda x:abs(x))[:k]

    P.sort()
    M.sort(reverse = True)
    p, m = [], []
    while len(p) + len(m) < k:
        if len(P) > 0 and len(M) <= 0: p.append(P.pop())
        elif len(P) <= 0 and len(M) > 0: m.append(M.pop())
        elif P[-1] < -M[-1]: m.append(M.pop())
        else: p.append(P.pop())
    if len(m)%2:
        Mi = M.pop() if len(p)*len(M) else 1  #  1 is no data
        Pi = P.pop() if len(m)*len(P) else -1 # -1 is no data
        if Mi < 0 and Pi >= 0:
            if abs(p[-1] * Pi) < abs(m[-1] * Mi):
                p.pop()
                m.append(Mi)
            else:
                m.pop()
                p.append(Pi)
        elif Mi < 0:
            p.pop()
            m.append(Mi)
        elif Pi >= 0:
            m.pop()
            p.append(Pi)
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
