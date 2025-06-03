import sys
from collections import deque
from bisect import bisect_left, bisect_right, insort_left, insort_right #func(リスト,値)
from heapq import heapify, heappop, heappush

sys.setrecursionlimit(10**6)
INF = 10**20

def mint():
    return map(int,input().split())
def lint():
    return map(int,input().split())
def judge(x, l=['Yes', 'No']):
    print(l[0] if x else l[1])

S = input()
N = len(S)+1
L = [0]*N
R = [0]*N
for i in range(N-1):
    L[i+1] = L[i]+1 if S[i]=='<' else 0
for i in range(N-2,-1,-1):
    R[i] = R[i+1]+1 if S[i]=='>' else 0
ans = [max(l,r) for l,r in zip(L,R)]
print(sum(ans))