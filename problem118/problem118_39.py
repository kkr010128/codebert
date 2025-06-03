import sys
#import time
#from collections import deque, Counter, defaultdict
#from fractions import gcd
import bisect
#import heapq
#import math
import itertools
input = sys.stdin.readline
sys.setrecursionlimit(10**8)
inf = 10**18
MOD = 1000000007
ri = lambda : int(input())
rs = lambda : input().strip()
rl = lambda : list(map(int, input().split()))

n = ri()  
ans=0    
for i in range(1,n+1):
    ans+=(n//i)*(n//i+1)*i//2
print(ans)