import math


def main():
    MOD = 10 ** 9 + 7
    N = int(input())
    A = list(map(int, input().split(' ')))
    # 答えは sum(lcm(A) / A)
    L = 1
    for a in A:
        L = L * a // math.gcd(L, a)
    ans = 0
    for a in A:
        ans += L * pow(a, MOD - 2, MOD)
        ans %= MOD
    print(ans)


if __name__ == '__main__':
    main()