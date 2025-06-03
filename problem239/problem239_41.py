import bisect,collections,copy,heapq,itertools,math,string
import numpy as np
import sys
sys.setrecursionlimit(10**7)

def _S(): return sys.stdin.readline().rstrip()
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def LS(): return list(sys.stdin.readline().rstrip().split())

C =_S()
#H,N= LI()
#AB = [LI() for _ in range(N)]
#A,B = zip(*AB)
#Ap = np.array(A)
#C = np.zeros(N + 1)

print(chr(ord(C)+1))

# if ans:
#     print('Yes')
# else:
#     print('No')