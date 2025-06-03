def main():
    N, M, K = [int(x) for x in input().split()]
    if M == 1:
        if K == N - 1:
            return 1
        else:
            return 0
    if N == 1:
        return M
    mod = 998244353
    fact = [1]
    for i in range(1, N):
        fact.append(fact[-1] * i % mod)
    fact_inv = [pow(fact[-1], mod - 2, mod)]
    for n in range(N - 1, 0, -1):
        fact_inv.append(fact_inv[-1] * n % mod)
    fact_inv = fact_inv[::-1]
    m_1_pow = [1]
    for _ in range(N):
        m_1_pow.append(m_1_pow[-1] * (M - 1) % mod)
    count = 0
    for k in range(K + 1):
        current = ((((m_1_pow[N - k - 1] * M) % mod) * fact[N - 1] % mod) * fact_inv[k] % mod) * fact_inv[N - 1 - k] % mod
        count = (count + current) % mod
    return count


if __name__ == "__main__":
    print(main())
