n=int(input())
import heapq
q=[]

for i in range(n):
    x,l=map(int,input().split())
    heapq.heappush(q,(x+l,l))

largest=-float('inf')
c=0
while q:
    a,l=heapq.heappop(q)
    if largest<=a-2*l:
        largest=a
        c+=1
print(c)