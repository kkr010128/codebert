import sys
import math
import collections

def set_debug(debug_mode=False):
    if debug_mode:
        fin = open('input.txt', 'r')
        sys.stdin = fin


def int_input():
    return list(map(int, input().split()))


def get(s):
    return str(s % 9) + '9' * (s // 9)

if __name__ == '__main__':
    # set_debug(True)

    # t = int(input())
    t = 1

    for ti in range(1, t + 1):
        n = int(input())
        A = int_input()

        cur = 0

        for x in A:
            cur = x ^ cur

        res = []
        for x in A:
            res.append(cur ^ x)

        print(*res)


