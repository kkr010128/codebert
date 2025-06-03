N, M = map(int, input().split())
a, w = 0, 0
P = set()
W = {}
for _ in range(M):
    p, S = map(str, input().split())
    if p in P:
        continue
    if S == 'WA':
        W.setdefault(p, 0)
        W[p] += 1
    if S == 'AC':
        a += 1
        P.add(p)
        if p in W:
            w += W[p]
print(a, w)