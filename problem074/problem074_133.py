N, K = map(int, input().split())
W = [0] * (N + 1)
W[1] = 1

R = []
for i in range(K):
    l, r = map(int, input().split())
    R.append((l, r))

MOD = 998244353
for i in range(1, N):
    for l, r in R:
        a = max(i - r, 0)
        b = i - l
        if b < 0:
            continue
        W[i + 1] += (W[b + 1] - W[a])
        W[i + 1] %= MOD
    W[i + 1] += W[i]
    
print(W[N] - W[N - 1])



