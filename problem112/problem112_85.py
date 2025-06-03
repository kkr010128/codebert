def solve():
    can_positive = False
    if len(P) > 0:
        if k < n: can_positive = True
        else: can_positive = len(M)%2 == 0
    else: can_positive = k%2 == 0

    if not can_positive: return sorted(P+M, key=lambda x:abs(x))[:k]
    P.sort()
    M.sort(reverse=True)
    a = [P.pop()] if k%2 else [1]
    while len(P) >= 2: a.append(P.pop() * P.pop())
    while len(M) >= 2: a.append(M.pop() * M.pop())
    return a[:1] + sorted(a[1:], reverse=True)[:(k-k%2)//2]

n, k = map(int, input().split())
P, M = [], []
for a in map(int, input().split()):
    if a < 0: M.append(a)
    else: P.append(a)
ans, MOD = 1, 10**9 + 7
for a in solve(): ans *= a; ans %= MOD
ans += MOD; ans %= MOD
print(ans)
