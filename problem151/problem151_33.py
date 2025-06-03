def modpow(a, x, mod):
    if x == 0:
        return 1
    elif x % 2 == 0:
        return modpow((a * a) % mod, x // 2, mod)
    else:
        return (modpow((a * a) % mod, x // 2, mod) * a) % mod


N, M, K = map(int, input().split(' '))
max_K = 3 * 10 ** 5
mod = 998244353

inv = [0 for i in range(max_K + 1)]
inv[0] = 1
inv[1] = 1
for i in range(2, K + 1):
    inv[i] = modpow(i, mod - 2, mod)
choose = [0 for i in range(K + 1)]
choose[0] = 1
for i in range(1, K + 1):
    choose[i] = choose[i - 1] * (((N - i) * inv[i]) % mod)
    choose[i] %= mod

ans = 0
for i in range(N - 1 - K, N):
    ans += modpow((M - 1), i, mod) * choose[N - i - 1]
    ans %= mod
print((ans * M) % mod)