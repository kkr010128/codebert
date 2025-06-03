N,K = map(int, input().split())

LR = list(tuple(map(int, input().split())) for _ in range(K))

S = [0]*(N+1)
S[1] = 1

for k in range(2, N+1):
    s = 0
    for l,r in LR:
        p0,p1 = max(k-r-1, 0), max(k-l, 0)
        s += S[p1] - S[p0]

    S[k] = (S[k-1] + s)%998244353

print((S[-1] - S[-2])%998244353)
