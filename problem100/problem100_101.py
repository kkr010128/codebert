from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

def main():
    X = int(input())

    if X <= 599:
        print('8')
    elif X <= 799:
        print('7')
    elif X <= 999:
        print('6')
    elif X <= 1199:
        print('5')
    elif X <= 1399:
        print('4')
    elif X <= 1599:
        print('3')
    elif X <= 1799:
        print('2')
    else:
        print('1')

if __name__ == '__main__':
    main()