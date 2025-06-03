# -*- coding:utf-8 -*-
import sys


def exhaustive(lst, size):
    result = []
    for i in range(0, 1 << size):
        total = 0
        for j in range(0, size):
            if (i & 0x01) == 1:
                total += lst[j]
            i = i >> 1
        result.append(total)
    return result


if __name__ == "__main__":
    lst = [val.split() for val in sys.stdin.read().splitlines()]
    n, data, m, targets = [[int(n) for n in inner_lst] for inner_lst in lst]
    result = exhaustive(data, int(n[0]))
    print("\n".join(["yes" if x in result else "no" for x in targets]))