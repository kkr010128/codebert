import fractions

from sys import stdin


def main():
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))
    sa = set(a)

    lcm = 1

    for ai in sa:
        lcm = (ai * lcm) // fractions.gcd(ai, lcm)

    ans = 0

    for ai in a:
        ans += lcm // ai
    ans %= 10 ** 9 + 7

    print(ans)


if __name__ == "__main__":
    main()
