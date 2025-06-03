N, K = map(int, input().split())
P = tuple(map(int, input().split()))

PMAX = 1000
s = [0] * (PMAX + 1)
for i in range(PMAX):
    s[i+1] = s[i] + (i + 1)

e = [0] * (N + 1)
for i, p in enumerate(P):
    e[i+1] = e[i] + (s[p] / p)

ans = 0
for i in range(N - K + 1):
    ans = max(ans, e[i+K] - e[i])
print(ans)