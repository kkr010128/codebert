import sys
from fractions import gcd

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60


def lcm(x, y):
    return x * y // gcd(x, y)


def main():
    N, M, *A = map(int, read().split())
    B = A[::]

    while not any(b % 2 for b in B):
        B = [b // 2 for b in B]

    if not all(b % 2 for b in B):
        print(0)
        return

    semi_lcm = 1
    for a in A:
        semi_lcm = lcm(semi_lcm, a // 2)

    print((M // semi_lcm + 1) // 2)
    return


if __name__ == '__main__':
    main()
