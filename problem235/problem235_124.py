def lcm(a, b):
    from fractions import gcd

    return a // gcd(a, b) * b


def main():
    _ = int(input())
    a = list(map(int, input().split()))
    x = 1

    for e in a:
        x = lcm(x, e)

    ans = 0
    for e in a:
        ans += x // e

    print(ans % int(1e9 + 7))


main()
