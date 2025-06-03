import heapq

n,k = map(int,input().split())
p = list(map(int,input().split()))

aa = heapq.nsmallest(k, p)
print(sum(aa))
