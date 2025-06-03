import bisect,collections,copy,heapq,itertools,math,string
import numpy as np
import sys
sys.setrecursionlimit(10**7)

def _S(): return sys.stdin.readline().rstrip()
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def LS(): return list(sys.stdin.readline().rstrip().split())

X = I()

# def is_prime(X,n):
#     # if n == 1:
#     #     return False
#     # for i in range(2,int(n**0.5)+1):
#     for i in range(2,X):
#         if n % i == 0:
#             return False
#     return True
def is_prime(n):
    # if n == 1:
    #     return False
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
            
for i in range(X,100003+1):
    # print(i)
    if is_prime(i):
        print(i)
        break

#H,N = LI()
#AB = [LI() for _ in range(N)]
#A,B = zip(*AB)
#Ap = np.array(A)
#C = np.zeros(N + 1)

# if ans:
#     print('Yes')
# else:
#     print('No')