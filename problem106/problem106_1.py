#!/usr/bin/env python
# -*- coding: utf-8 -*-


def main():
    N = int(input())
    ans = [0] * (6 * 10**4 + 10)

    for x in range(1, 101):
        for y in range(1, 101):
            for z in range(1, 101):
                ans[x**2 + y**2 + z**2 + x * y + y * z + x * z - 1] += 1

    for i in range(N):
        print(ans[i])


if __name__ == "__main__":
    main()
