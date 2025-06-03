N, K = map(int, input().split())
N += 1
ans = 0
p = 10 ** 9 + 7

for k in range(K, N + 1):
    ans += (k * (N - k) + 1) % p
    ans %= p

print(ans)