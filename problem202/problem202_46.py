from sys import stdin, setrecursionlimit
from collections import Counter, deque, defaultdict
from math import floor, ceil
from bisect import bisect_left
from itertools import combinations
setrecursionlimit(100000)

INF = int(1e10)
MOD = int(1e9 + 7)

def main():
    from builtins import int, map
    N, A, B = map(int, input().split())
    if A == 0:
        print(0)
        exit()

    ans = (N // (A + B)) * A
    if N % (A + B) > 0:
        ans += min(N % (A + B), A)
    print(ans)

if __name__ == '__main__':
    main()
