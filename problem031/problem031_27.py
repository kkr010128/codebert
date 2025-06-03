# coding=utf-8
from __future__ import division
from  math import sqrt


def mean(list_):
    return sum(list_) / len(list_)


def std(list_):
    m = mean(list_)
    return sqrt(sum([(x - m) ** 2 for x in list_]) / len(list_))

def main():
    n = input()
    while n:
        scores = map(int, raw_input().split())
        print std(scores)
        n = input()


if __name__ == '__main__':
    main()