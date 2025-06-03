# -*- coding: utf-8 -*-
from sys import stdin
input = stdin.readline


def main():
    a, b, c, d = list(map(int,input().split()))
    print(max([a*c, a*d, b*c, b*d]))

if __name__ == "__main__":
    main()
