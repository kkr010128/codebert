from heapq import heappush,heappop
n=int(input())
a=list(map(int,input().split()))
b=[]
for i in range(n):
  heappush(b,(a[i],i+1))
a=[]
for i in range(n):
  c,d=heappop(b)
  a.append(d)
print(*a)