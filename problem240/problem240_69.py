import bisect,collections,copy,heapq,itertools,math,string
import numpy as np
import sys
sys.setrecursionlimit(10**7)

def _S(): return sys.stdin.readline().rstrip()
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def LS(): return list(sys.stdin.readline().rstrip().split())

# N =I()
N,M= LI()
if M==0:
    print(0,0)
    exit()
pS = [LS() for _ in range(M)]
# print(pS)

_p,S = zip(*pS)

p = list(map(int,_p))

WA = np.zeros(N+1)
AC = np.full(N+1,False, dtype=bool)

penalty = 0
for i in range(M):
    if AC[p[i]]:
        continue
    if S[i]=='WA':
        WA[p[i]] += + 1
    else:
        AC[p[i]]=True
        penalty += WA[p[i]]        

AC_count = np.count_nonzero(AC)        

# space output
print(AC_count,int(penalty))

#Ap = np.array(A)



# if ans:
#     print('Yes')
# else:
#     print('No')