import sys

input = sys.stdin.readline
P = 10 ** 9 + 7


def main():
    N, K = map(int, input().split())

    ans = 0
    n_gcd = [0] * (K + 1)
    for k in reversed(range(1, K + 1)):
        n = pow(K // k, N, mod=P)
        for kk in range(2 * k, K + 1, k):
            n -= n_gcd[kk]
        n_gcd[k] = n % P
        ans += k * n_gcd[k]
        ans %= P

    print(ans)


if __name__ == "__main__":
    main()
