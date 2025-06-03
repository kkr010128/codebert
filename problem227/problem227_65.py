from sys import exit
import math
import collections
ii = lambda : int(input())
mi = lambda : map(int,input().split())
li = lambda : list(map(int,input().split()))

n,k = mi()
h = li()
h.sort()
h.reverse()
sum = 0
for i in range(k,n,1):
    sum += h[i]
print(sum)
