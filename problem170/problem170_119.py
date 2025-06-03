N, K = map(int, input().split())
ans = 0
mod = 10 ** 9 + 7
for k in range(K, N + 2):
    max_range = int(k * (2 * N - k + 1) / 2)
    min_range = int((k-1) * k / 2)
    tmp = (max_range - min_range + 1) % mod
    ans += tmp
    ans %= mod

print(ans)
