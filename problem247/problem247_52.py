import sys
from math import gcd
from functools import reduce
import numpy as np
    
read = sys.stdin.read
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7


def lcm_base(a, b):
    return (a * b) // gcd(a, b)


def lcm_list(numbers):
    return reduce(lcm_base, numbers, 1)


def main():
    n, m = map(int, readline().split())
    a = np.array(input().split(), np.int64)
    a //= 2
    b = np.copy(a)
    while True:
        c = b % 2
        if c.sum() == 0:
            b //= 2
        elif c.sum() == n:
            break
        else:
            print(0)
            sys.exit()
    d = lcm_list(a)
    if d > 10 ** 9:
        ans = 0
    else:
        ans = (m // d) - (m // (d + d))
    print(ans)


if __name__ == '__main__':
    main()
