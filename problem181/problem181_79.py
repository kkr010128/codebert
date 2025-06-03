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

queue = deque()


def main():
    k = int(input())
    queue.extend([1, 2, 3, 4, 5, 6, 7, 8, 9])

    for i in range(k-1):
        x = queue[0]
        queue.popleft()
        if x % 10 != 0:
            queue.append(10 * x + x % 10 - 1)
        queue.append(10 * x + x % 10)
        if x % 10 != 9:
            queue.append(10 * x + x % 10 + 1)
    print(queue[0])


if __name__ == '__main__':
    main()
