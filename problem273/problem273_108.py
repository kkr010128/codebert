ma = lambda :map(int,input().split())
lma = lambda :list(map(int,input().split()))
tma = lambda :tuple(map(int,input().split()))
ni = lambda:int(input())
yn = lambda fl:print("Yes") if fl else print("No")
import collections
import math
import itertools
import heapq as hq
n,k = ma()
A = lma()
s = [0]*(n+1)
l = [0]*(n+1)
for i in range(n):
    s[i+1]=(s[i]+A[i])%k
    l[i+1]=(s[i+1]-(i+1))%k
ans = 0
co = collections.Counter(l[:min(n+1,k)])
for num,cnt in co.items():
    ans+=cnt*(cnt-1)//2
for i in range(k,n+1):
    co[l[i-k]]-=1
    ans+=co[l[i]]
    co[l[i]]+=1



print(ans)
