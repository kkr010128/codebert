import sys, bisect, math, itertools, heapq, collections
from operator import itemgetter
# a.sort(key=itemgetter(i)) # i番目要素でsort
from functools import lru_cache
# @lru_cache(maxsize=None)
sys.setrecursionlimit(10**8)
input = sys.stdin.readline
INF = float('inf')
mod = 10**9+7
eps = 10**-7
def inp():
    '''
    一つの整数
    '''
    return int(input())
def inpl():
    '''
    一行に複数の整数
    '''
    return list(map(int, input().split()))

n, k, c = inpl()
s = list(input())[:-1]
q = collections.deque()
cool = 0
left = [0] * n
right = [0] * n
val=-1
for i in range(n):
    if cool<=0 and s[i]=="o" and val<k:
        val += 1
        cool = c
    else:
        cool-=1
    left[i] = val
cool = 0
val+=1
for i in range(n-1,-1,-1):
    if cool<=0 and s[i]=="o" and val>0:
        val -= 1
        cool = c
    else:
        cool-=1
    right[i]=val
# print(left)
# print(right)
for i in range(n):
    if left[i]==right[i] and (i == 0 or left[i] - left[i - 1] == 1) and (i == n - 1 or right[i + 1] - right[i] == 1):
        print(i + 1)
