import sys
import math
import heapq
mod=10**9+7
inf=float("inf")
from math import sqrt
from collections import deque
from collections import Counter
from math import ceil
input=lambda: sys.stdin.readline().strip()
sys.setrecursionlimit(11451419)
from functools import lru_cache
#メモ化再帰defの冒頭に毎回 @lru_cache(maxsize=10**10)
#引数にlistはだめ
#######ここまでテンプレ#######
#######ここから天ぷら########
import fractions as math
from functools import reduce
def lcm_base(x, y):
    return (x * y) // math.gcd(x, y)

def lcm(*numbers):
    return reduce(lcm_base, numbers, 1)

def qq(numbers):
    return reduce(lcm_base, numbers, 1)

n,m=map(int,input().split())
A=list(map(int,input().split()))

B=[i//2 for i in A]
p=qq(B)
for i in A:
    i//=2
    if (p//i)%2==0:
        print(0)
        exit()
print(m//p - m//(p*2))
