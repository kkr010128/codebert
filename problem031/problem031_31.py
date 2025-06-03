# coding=utf-8
from __future__ import division
from  math import sqrt


def main():
    n = input()
    while n:
        scores = map(int, raw_input().split())
        m = sum(scores) / n
        print sqrt(sum([(x - m) ** 2 for x in scores]) / n)
        n = input()


if __name__ == '__main__':
    main()