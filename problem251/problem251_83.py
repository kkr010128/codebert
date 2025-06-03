# coding=UTF-8
from collections import deque
from operator import itemgetter
from bisect import bisect_left, bisect
import itertools
import sys
import math
import numpy as np
import time
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def main():
    n, k = map(int, input().split())
    r, s, p = map(int, input().split())
    t = input()

    myhand = [None] * n
    point = 0

    for i in range(n):
        if t[i] == "r":
            if myhand[i] != "np":
                point += p
                if i+k < n:
                    myhand[i+k] = "np"
            else:
                if i+k < n:
                    myhand[i + k] = None
        elif t[i] == "s":
            if myhand[i] != "nr":
                point += r
                if i+k < n:
                    myhand[i+k] = "nr"
            else:
                if i+k < n:
                    myhand[i + k] = None
        elif t[i] == "p":
            if myhand[i] != "ns":
                point += s
                if i+k < n:
                    myhand[i+k] = "ns"
            else:
                if i+k < n:
                    myhand[i + k] = None

    print(point)


if __name__ == '__main__':
    main()
