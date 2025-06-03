import heapq
N,K = map(int,input().split())
Hlist = list(map(int,input().split()))
for i in range(len(Hlist)):
    Hlist[i] *= -1
heapq.heapify(Hlist)
for _ in range(min(K,N)):
    heapq.heappop(Hlist)
print(-sum(Hlist))