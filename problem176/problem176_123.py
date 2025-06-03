MOD = 10 ** 9 + 7
N, K = map(int, input().split())

# cnt(n): gcd = n となる数列の個数
cnt = [0] * (K + 1)

# A1,...,ANのすべてがxの倍数である数列の個数 = floor(k/x)^N個
for n in range(1, K + 1):
    cnt[n] = pow(K // n, N, MOD)

res = 0
for k in range(K, 0, -1):
    p = 2
    while p * k <= K:
        cnt[k] -= cnt[p * k]
        cnt[k] %= MOD
        p += 1
    res += cnt[k] * k
    res %= MOD

print(res)
