from collections import Counter, defaultdict
import sys

sys.setrecursionlimit(10 ** 5 + 10)
# input = sys.stdin.readline
from math import factorial
import heapq, bisect
import math
import itertools

import queue
from collections import deque


def main():
    num, submit = map(int, input().split())
    fin_flg = [0 for i in range(num + 1)]
    count_ac, count_wa = 0, 0

    for i in range(submit):
        a, b = input().split()
        a = int(a)
        if fin_flg[a] == -1:
            continue
        if b == "AC":
            count_ac += 1
            count_wa += fin_flg[a]
            fin_flg[a] = -1
        else:
            fin_flg[a] += 1

    print(count_ac, count_wa)




if __name__ == '__main__':
    main()
