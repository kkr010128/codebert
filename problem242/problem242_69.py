MOD = 10 ** 9 + 7
table_len = 10 ** 5 + 10

fac = [1, 1]
for i in range(2, table_len):
    fac.append(fac[-1] * i % MOD)

finv = [0] * table_len
finv[-1] = pow(fac[-1], MOD - 2, MOD)
for i in range(table_len-1, 0, -1):
    finv[i-1] = finv[i] * i % MOD


def sum_of_maxS(N, K, As):
    ret = 0
    for i in range(N - K + 1):
        ret += ((As[i] * fac[N - i - 1]) % MOD) * \
            ((finv[K-1] * finv[N - K - i]) % MOD) % MOD
        ret %= MOD
    return ret


N, K = map(int, input().split())
As = sorted(map(int, input().split()), reverse=True)

minus_As = [-A for A in reversed(As)]

print((sum_of_maxS(N, K, As) + sum_of_maxS(N, K, minus_As)) % MOD)
