from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    for i in range(N-K):
        if A[i] < A[i+K]:
            print('Yes')
        else:
            print('No')

if __name__ == '__main__':
    main()