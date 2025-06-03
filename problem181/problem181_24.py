import sys, bisect, math, itertools, string, queue, copy
import numpy as np
import scipy
from collections import Counter,defaultdict,deque
from itertools import permutations, combinations
from heapq import heappop, heappush
from fractions import gcd
input = sys.stdin.readline
sys.setrecursionlimit(10**8)
mod = 10**9+7
def inp(): return int(input())
def inpm(): return map(int,input().split())
def inpl(): return list(map(int, input().split()))
def inpls(): return list(input().split())
def inplm(n): return list(int(input()) for _ in range(n))
def inplL(n): return [list(input()) for _ in range(n)]
def inplT(n): return [tuple(input()) for _ in range(n)]
def inpll(n): return [list(map(int, input().split())) for _ in range(n)]
def inplls(n): return sorted([list(map(int, input().split())) for _ in range(n)])

k = inp()

runrun = [["1","2","3","4","5","6","7","8","9"]]
runrun_int = []

for j in range(2,11):
    tmp = []
    for i in range(len(runrun[j - 2])):
        if runrun[j-2][i][j-2] == "0":
            tmp.append(runrun[j-2][i] + str(int(runrun[j-2][i][j-2])))
            tmp.append(runrun[j-2][i] + str(int(runrun[j-2][i][j-2]) + 1))
        elif runrun[j-2][i][j-2] in ["1","2","3","4","5","6","7","8"]:
            tmp.append(runrun[j-2][i] + str(int(runrun[j-2][i][j-2]) - 1))
            tmp.append(runrun[j-2][i] + str(int(runrun[j-2][i][j-2])))
            tmp.append(runrun[j-2][i] + str(int(runrun[j-2][i][j-2]) + 1))
        elif runrun[j-2][i][j-2] == "9":
            tmp.append(runrun[j-2][i] + str(int(runrun[j-2][i][j-2]) - 1))
            tmp.append(runrun[j-2][i] + str(int(runrun[j-2][i][j-2])))
    runrun.append(tmp)

ans = []
for i in range(len(runrun)):
    for j in range(len(runrun[i])):
        ans.append(int(runrun[i][j]))
ans.sort()

print(ans[k - 1])