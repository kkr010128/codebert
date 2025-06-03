def main():
    N, K = map(int, input().split())
    mod = 10**9 + 7
    r = 0
    D = [0] * (K + 1)
    for i in reversed(range(1, K + 1)):
        D[i] = pow(K // i, N, mod) - sum(D[::i])
    return sum(i * j for i, j in enumerate(D)) % mod

print(main())
