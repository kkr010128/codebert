# https://atcoder.jp/contests/abc163/tasks/abc163_d

def main():
    MOD = 10**9 + 7
    n, k = [int(i) for i in input().strip().split()]
    table = [0] * (n + 2)
    table[1] = 1

    for i in range(2, n + 1):
        table[i] = table[i - 1] + i

    ans = 0
    for i in range(k, n + 1):
        _min = table[i - 1]
        _max = table[n] - table[n - i]
        ans += _max - _min + 1
        ans %= MOD
    print((ans + 1) % MOD)


if __name__ == "__main__":
    main()
