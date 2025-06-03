# coding=utf-8
from __future__ import division
from math import sqrt


def main():
    d = input()
    x = map(int, raw_input().split())
    y = map(int, raw_input().split())
    z = [x - y for x, y in zip(x, y)]
    print sum([abs(w) for w in z])
    print sqrt(sum([w ** 2 for w in z]))
    print sum([abs(w) ** 3 for w in z]) ** (1 / 3)
    print max([abs(w) for w in z])


if __name__ == '__main__':
    main()