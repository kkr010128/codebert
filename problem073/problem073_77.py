#!/usr/bin/env python
from typing import List


def input_int() -> int:
    return int(input())


def input_list_int() -> List[int]:
    return list(map(lambda x: int(x), input().split()))


def f(n: int) -> int:
    ans = 0
    for a in range(1, n):
        ans += (n - 1) // a
    return ans


if __name__ == '__main__':
    n = input_int()
    print(f(n))