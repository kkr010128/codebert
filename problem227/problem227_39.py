import heapq
(N,K) = map(int,input().split())
h = [int(x)*-1 for x in input().split()]
ans = 0
heapq.heapify(h)
if K <= N:
    for i in range(K):
        heapq.heappop(h)

    while h != []:
        ans -= heapq.heappop(h)

print(ans)