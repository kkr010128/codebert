# -*- coding: utf-8 -*-
from sys import stdin
input = stdin.readline


def main():
    n = int(input().strip())
    print('1' if n == 0 else '0')

if __name__ == "__main__":
    main()
