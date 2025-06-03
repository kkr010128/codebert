import sys
from sys import exit
from collections import deque
from bisect import bisect_left, bisect_right, insort_left, insort_right #func(リスト,値)
from heapq import heapify, heappop, heappush
from math import *

sys.setrecursionlimit(10**6)
INF = 10**20
MOD = 10**9+7

def mint():
    return map(int,input().split())
def lint():
    return list(map(int,input().split()))
def judge(x, l=['Yes', 'No']):
    print(l[0] if x else l[1])
def lprint(l, sep='\n'):
    for x in l:
        print(x, end=sep)

N,A = int(input()),lint()
S = dict()
for a in A:
    S.setdefault(a,0)
    S[a] += 1
ans = 0
for k in S:
    ans += S[k]*(S[k]-1)//2
for a in A:
    print(ans-(S[a]-1))