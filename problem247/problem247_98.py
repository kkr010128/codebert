from math import gcd
from functools import reduce
import sys
input = sys.stdin.readline


def lcm(a, b):
    return a*b // gcd(a, b)


def count_factor_2(num):
    count = 0
    while num % 2 == 0:
        num //= 2
        count += 1
    return count


def main():
    n, m = map(int, input().split())
    A = list(map(lambda x: x//2, set(map(int, input().split()))))

    check = len(set(map(count_factor_2, A)))
    if check != 1:
        print(0)
        return

    lcm_a = reduce(lcm, A)
    step = lcm_a * 2
    ans = (m + lcm_a) // step
    print(ans)


if __name__ == "__main__":
    main()
