#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys


def get_ints():
    return map(int, sys.stdin.readline().strip().split())


def main():
    L, R, d = get_ints()
    ans = 0
    for i in range(L, R + 1):
        if i % d == 0:
            ans += 1
    print(ans)


if __name__ == "__main__":
    main()
