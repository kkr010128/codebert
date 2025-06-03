import numpy as np

MOD = 10 ** 9 + 7
N, K = map(int, input().split(' '))

cumsum = np.arange(0, N + 2).cumsum()

ans = 0
for k in range(K, N + 2):
    ans += cumsum[-1] - cumsum[-(k + 1)] - cumsum[k] + 1
    ans %= MOD

print(ans)
