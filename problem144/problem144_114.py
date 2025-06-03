import bisect,collections,copy,heapq,itertools,math,string
import numpy as np
import sys
from cmath import pi, rect
sys.setrecursionlimit(10**7)

def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))

A,B,H,M = LI()

H += M / 60
H = H/12 * 2*pi
M = M/60 * 2*pi

# 余弦定理
l = math.sqrt(A**2 + B**2 - 2*A*B*math.cos(H-M) )
 
# 複素数座標 Aexp(iθ)
zA = A * np.exp(H*1j)
zB = B * np.exp(M*1j)

l=abs(zA - zB)

print(l)
