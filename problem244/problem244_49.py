'''
https://atcoder.jp/contests/abc150/tasks/abc150_c
'''
def main():
    import sys
    #input = sys.stdin.readline
    sys.setrecursionlimit(10000000)
    from collections import Counter, deque
    #from collections import defaultdict
    from itertools import combinations, permutations
    #from itertools import accumulate, product
    from math import floor, ceil
    #from operator import itemgetter

    #mod = 1000000007

    k, x = map(int, input().split())
    if k*500>=x:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()