MOD = 10**9 + 7


def main():
    import sys
    input = sys.stdin.buffer.readline
    _ = int(input())
    A = [int(i) for i in input().split()]

    def gcd(x, y):
        if y == 0:
            return x
        while y != 0:
            x, y = y, x % y
        return x

    def lcm(x, y):
        return x*y//gcd(x, y)

    L = A[0]
    for a in A[1:]:
        L = lcm(L, a)
    L %= MOD
    ans = 0
    for a in A:
        ans += L*pow(a, MOD-2, MOD)
    print(ans % MOD)


if __name__ == '__main__':
    main()
