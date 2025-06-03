import math
import numpy as np
import sys
import os
from operator import mul
from operator import itemgetter

sys.setrecursionlimit(10**7)

def _S(): return sys.stdin.readline().rstrip()
def I(): return int(_S())
def LS(): return list(_S().split())
def LI(): return list(map(int,LS()))

if os.getenv("LOCAL"):
    inputFile = basename_without_ext = os.path.splitext(os.path.basename(__file__))[0]+'.txt'
    sys.stdin = open(inputFile, "r")
INF = float("inf")
IINF = 10 ** 18
MOD = 10 ** 9 + 7
# MOD = 998244353    

N,M = LI()
H = LI()
AB = [LI() for _ in range(M)]

p = []
d = {}
for i in range(N):
    # p.append((i,H[i]))
    d[i]=H[i]
# p.sort(key=itemgetter(1),reverse=True)
# print(p)
# print(d)

# g = np.zeros(shape=(N,N),dtype='int')
g = [set()] * N
a = [True] * N

for i in range(M):
    f = AB[i][0]-1
    t = AB[i][1]-1
    if d[t]>d[f]:
        a[f]=False
    elif d[f]>d[t]:
        a[t]=False
    else:
        a[f]=False
        a[t]=False
# print(a)
print(sum(a))  
    # print(g[f])
    # g[f] = np.append(g[f],t)
    # g[t] = np.append(g[t],f)
   
    # g[f][t]=1
    # g[t][f]=1

# print(g)
# list.sort(key=itemgetter(0))

# for i in range(N):


# a = np.where(g[0]==1)
# print(a)