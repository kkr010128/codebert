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
from fractions import Fraction



def main():
    num = int(input())
    data = list(map(int, input().split()))

    now_ind = 1
    break_num = 0

    for i in range(num):
        if data[i] == now_ind:
            now_ind += 1
        else:
            break_num += 1

    if break_num == num:
        print(-1)
    else:
        print(break_num)



if __name__ == '__main__':
    main()

