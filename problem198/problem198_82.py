import sys
input=sys.stdin.readline
sys.setrecursionlimit(10 ** 7)
from itertools import accumulate
from itertools import permutations
from itertools import combinations
from collections import defaultdict
from collections import Counter
import fractions
import math
from collections import deque
from bisect import bisect_left
from bisect import insort_left
import itertools
from heapq import heapify
from heapq import heappop
from heapq import heappush
import heapq
import numpy as np
INF = float("inf")
#d = defaultdict(int)
#d = defaultdict(list)
#N = int(input())
#A = list(map(int,input().split()))
#S = list(input())
#S.remove("\n")
#N,M = map(int,input().split())
#S,T = map(str,input().split())
#A = [int(input()) for _ in range(N)]
#S = [input() for _ in range(N)]
#A = [list(map(int,input().split())) for _ in range(N)]
N = int(input())
if N == 1:
    print("a")
else:
    S = list("abcdefghij")
    Q = deque([("a",1)])  #文字列、種類
    while len(Q) != 0:
        s,kind = Q.popleft()
        for i in range(kind+1):
            news = s+S[i]
            if len(news) == N+1:
                break
            if len(news) == N:
                print(news)
            if i == kind:
                Q.append((news,kind+1))
            else:
                Q.append((news,kind))