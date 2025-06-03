n=int(input())
xy=[list(map(int,input().split())) for _ in range(n)]
from itertools import permutations
ans=0
for i in permutations(range(n),n):
    for j in range(1,n):
        ans+=((xy[i[j]][0]-xy[i[j-1]][0])**2+(xy[i[j]][1]-xy[i[j-1]][1])**2)**0.5
for i in range(1,n+1):
    ans/=i
print(ans)

        
