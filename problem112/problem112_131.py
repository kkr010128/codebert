def solve():
    if k==n: return P + M
    if len(M) == n: return sorted(M, reverse=k%2)[:k]

    P.sort(reverse=True)
    M.sort()
    P.append(-1)
    M.append(1) # add endpoint
    pa, ma = [], []
    while len(pa) + len(ma) < k:
        if P[len(pa)] < -M[len(ma)]:
            ma.append(M[len(ma)])
        else:
            pa.append(P[len(pa)])

    if len(ma)%2 == 0: return pa + ma

    exist_pa = len(pa) > 0
    exist_ma = len(ma) > 0
    remain_p = len(P) - 1 > len(pa)
    remain_m = len(M) - 1 > len(ma)
    if exist_pa & exist_ma & remain_p & remain_m:
        if abs(pa[-1] * P[len(pa)]) < abs(ma[-1] * M[len(ma)]):
            pa.pop()
            ma.append(M[len(ma)])
        else:
            ma.pop()
            pa.append(P[len(pa)])
    elif exist_ma & remain_p:
        ma.pop()
        pa.append(P[len(pa)])
    elif exist_pa & remain_m:
        pa.pop()
        ma.append(M[len(ma)])
    return pa + ma

n, k = map(int, input().split())
P, M = [], [] # plus, minus
for a in map(int, input().split()):
    if a < 0: M.append(a)
    else: P.append(a)
ans, MOD = 1, 10**9 + 7
for a in solve(): ans *= a; ans %= MOD
ans += MOD; ans %= MOD
print(ans)
