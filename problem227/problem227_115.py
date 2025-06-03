import sys
#import string
#from collections import defaultdict, deque, Counter
#import bisect
#import heapq
#import math
#from itertools import accumulate
#from itertools import permutations as perm
#from itertools import combinations as comb
#from itertools import combinations_with_replacement as combr
#from fractions import gcd
#import numpy as np

stdin = sys.stdin
sys.setrecursionlimit(10 ** 7)
MIN = -10 ** 9
MOD = 10 ** 9 + 7
INF = float("inf")
IINF = 10 ** 18

def solve():
    #n = int(stdin.readline().rstrip())
    n,k = map(int, stdin.readline().rstrip().split())
    H = list(map(int, stdin.readline().rstrip().split()))
    #numbers = [[int(c) for c in l.strip().split()] for l in sys.stdin]
    #word = [stdin.readline().rstrip() for _ in range(n)]
    #number = [[int(c) for c in stdin.readline().rstrip()] for _ in range(n)]
    #zeros = [[0] * w for i in range(h)]
    H.sort()
    if n <= k:
        print(0)
        exit()

    for i in range(k):
        H.pop(-1)

    print(sum(H))

if __name__ == '__main__':
    solve()
