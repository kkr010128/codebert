n=int(input())
a=[-int(j) for j in input().split()]
a.sort()
import heapq
l=[a[0]]
heapq.heapify(l)
ans=0
for i in a[1:]:
    heapq.heappush(l,i)
    heapq.heappush(l,i)
    p=heapq.heappop(l)
    ans-=p
print(ans)