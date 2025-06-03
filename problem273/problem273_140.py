from collections import defaultdict

N, K, *A = map(int, open(0).read().split())

x = [0] * (N + 1)
for i in range(N):
    x[i + 1] = x[i] + A[i]
    
y = [(x[i] - i) % K for i in range(N + 1)]

ctr = defaultdict(int)
ans = 0
for j in range(N + 1):
    ans += ctr[y[j]]
    ctr[y[j]] += 1
    if j - K + 1 >= 0:
        ctr[y[j - K + 1]] -= 1
print(ans)
