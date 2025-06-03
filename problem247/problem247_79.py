import sys
from fractions import gcd

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60


def lcm(a, b):
    return a * b // gcd(a, b)


def main():
    N, M, *A = map(int, read().split())
    A = list({a // 2 for a in A})

    power = 1
    while all(a % 2 == 0 for a in A):
        A = [a // 2 for a in A]
        power *= 2

    if any(a % 2 == 0 for a in A):
        print(0)
        return

    l = 1
    for a in A:
        l = lcm(l, a)

    l *= power
    ans = (M + l) // (2 * l)
    print(ans)
    return


if __name__ == '__main__':
    main()
