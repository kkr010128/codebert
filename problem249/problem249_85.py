from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

def main():
    A, B, K = map(int, input().split())

    if A >= K:
        print(A - K, B)
    elif A < K:
        if K - A >= B:
            print(0, 0)
        else:
            print(0, B - (K - A))

if __name__ == '__main__':
    main()