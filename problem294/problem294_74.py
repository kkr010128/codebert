import bisect,collections,copy,heapq,itertools,math,string
import numpy as np
import sys
sys.setrecursionlimit(10**7)

def _S(): return sys.stdin.readline().rstrip()
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def LS(): return list(sys.stdin.readline().rstrip().split())

N = I()
L = LI()
# L = np.array(_L)
#C = np.zeros(N + 1)

# def test(a,b,c):
#     if a<b+c and b<c+a and c<a+b:
#         return True
#     return False

# count = 0
# for pair in itertools.combinations(L, 3):
#     # print(pair)
#     if test(*pair):
#         count += 1
# print(count)

# for i in range(N):
#     for j in range(i+1,N):

from numba import njit
 
@njit
def f(A):
  count = 0
  for i in range(N):
    for j in range(i + 1, N):
      for k in range(j + 1, N):
        count += (A[k] < A[i] + A[j])
  return count
 
A = np.array(L)
A.sort()
print(f(A))        
