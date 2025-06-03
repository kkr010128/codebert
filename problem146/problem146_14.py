from collections import defaultdict
import math


def ggg(a, b):
    """規約分数を作る。n/0, 0/n は n=1,-1 にして返す。"""
    if a == b == 0:
        return 0, 0

    denominator = math.gcd(a, b)
    x, y = a // denominator, b // denominator
    return x, y


def main():
    n = int(input())
    mod = 1000000007
    zeroes = 0
    counter = defaultdict(lambda: defaultdict(int))
    for _ in range(n):
        a, b = [int(x) for x in input().split()]
        x, y = ggg(a, b)

        if x == y == 0:
            zeroes += 1
            continue
        if y < 0:
            # quadrant III, IV -> I, II
            x, y = -x, -y

        if x <= 0:
            # round 90° from quadrant II to I
            x, y = y, -x
            counter[(x, y)][1] += 1
        else:
            counter[(x, y)][0] += 1

    ans = 1
    for v in counter.values():
        now = 1
        now += pow(2, v[0], mod) - 1
        now += pow(2, v[1], mod) - 1
        ans = ans * now % mod
    ans += zeroes
    ans -= 1  # choose no fish
    return ans % mod


if __name__ == '__main__':
    print(main())
