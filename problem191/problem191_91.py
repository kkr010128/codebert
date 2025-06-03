#!/usr/bin/env python3
import sys


def solve(L: int):
    return (L / 3) ** 3


def main():
    L = int(sys.stdin.readline().strip())  # type: int
    print(solve(L))


if __name__ == '__main__':
    main()
