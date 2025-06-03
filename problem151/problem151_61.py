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
    count = 0
    for k in range(K + 1):
        current = pow(M - 1, N - k - 1, mod) * M % mod
        rev = pow(fact[k] * fact[N - 1 - k] % mod, mod - 2, mod)
        current = (current * fact[N - 1] % mod) * rev % mod
        count = (count + current) % mod
    return count


if __name__ == "__main__":
    print(main())
