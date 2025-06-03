import sys
import math
from functools import reduce


def num_of_zeros(num):
    return (num ^ (num - 1)).bit_length() - 1


def lcm_base(x, y):
    return (x * y) // math.gcd(x, y)


def lcm_list(numbers):
    return reduce(lcm_base, numbers, 1)


def main():
    input = sys.stdin.buffer.readline
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    if len(set(map(num_of_zeros, a))) != 1:
        print(0)
    else:
        lcm = lcm_list(list(map(lambda x: x // 2, a)))
        ub = 10 ** 9
        lb = 0
        while ub - lb > 1:
            mid = (ub + lb) // 2
            if lcm * (2 * mid + 1) <= m:
                lb = mid
            else:
                ub = mid
        if lcm <= m:
            lb += 1
        print(lb)


if __name__ == "__main__":
    main()
