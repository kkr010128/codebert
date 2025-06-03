import math
import itertools

n=int(input())
d=[list(map(int,input().split())) for _ in range(n)]

ans=cnt=0
for i in itertools.permutations([_ for _ in range(n)]):
  for j in range(n-1):
    x1,x2=d[i[j]][0],d[i[j+1]][0]
    y1,y2=d[i[j]][1],d[i[j+1]][1]
    ans+=math.sqrt((x1-x2)**2+(y1-y2)**2)
  cnt+=1
  #print(j,ans,cnt)
print(ans/cnt)