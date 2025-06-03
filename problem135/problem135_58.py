import bisect,collections,copy,heapq,itertools,math,string,decimal
import numpy as np
import sys
sys.setrecursionlimit(10**7)

def _S(): return sys.stdin.readline().rstrip()
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def LS(): return list(sys.stdin.readline().rstrip().split())


# N = I()
_A,_B = LS()
A = decimal.Decimal(_A)
B = decimal.Decimal(_B)

print((A*B).quantize(decimal.Decimal('0'), rounding=decimal.ROUND_DOWN))

#AB = [LI() for _ in range(N)]
#A,B = zip(*AB)
#Ap = np.array(A)
#C = np.zeros(N + 1)

# if ans:
#     print('Yes')
# else:
#     print('No')