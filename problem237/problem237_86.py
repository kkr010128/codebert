import heapq
n=int(input())
rb = []
heapq.heapify(rb)
for i in range(n):
    x,l= map(int,input().split())
    heapq.heappush(rb,(x+l,x-l))
ans=0
mostr=-1
while len(rb)>0:
    c=heapq.heappop(rb)
    if ans==0:
        ans+=1
        mostr=c[0]
    else:
        if mostr<=c[1]:
            ans+=1
            mostr=c[0]
print(ans)