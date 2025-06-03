import bisect,collections,copy,heapq,itertools,math,string
import numpy as np
from numba import njit
import sys
sys.setrecursionlimit(10**7)

def _S(): return sys.stdin.readline().rstrip()
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def LS(): return list(sys.stdin.readline().rstrip().split())

N,K = LI()
p = LI()
p.sort()
p1 = np.array(p)
print(p1[:K].sum())
