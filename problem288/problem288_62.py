import bisect,collections,copy,heapq,itertools,math,string
import numpy as np
import sys
sys.setrecursionlimit(10**7)

def _S(): return sys.stdin.readline().rstrip()
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def LS(): return list(sys.stdin.readline().rstrip().split())

# 最短距離
# 素因数分解
N = I()

def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    divisors.sort()
    return divisors

# c = sympy.divisors(N)
c = make_divisors(N)
lenc = len(c)
if (lenc % 2)==0:
    a = c[lenc // 2 - 1]
    b = c[lenc // 2]
else:
    a = c[lenc // 2]
    b = a

print(a + b -2)

#H,N = LI()
#AB = [LI() for _ in range(N)]
#A,B = zip(*AB)
#Ap = np.array(A)
#C = np.zeros(N + 1)

# if ans:
#     print('Yes')
# else:
#     print('No')