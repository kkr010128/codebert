N, K = map(int, input().split())
p = list(map(int, input().split()))
E = [0] * N
for i in range(N):
    P = 0.5 * p[i] * (p[i] + 1)
    E[i] = P / p[i]
S = sum(E[:K])
s = S
for i in range(N - K):
    s -= E[i]
    s += E[i + K]
    S = max(S, s)
print(S)