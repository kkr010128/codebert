a=int(input())
b=[list(map(int,input().split())) for i in range(a)]
c=[[i[0]-i[1],i[0]+i[1]] for i in b]
c.sort(key=lambda x: x[1])
ans=0
right=-10**9-1
for i in range(a):
    if right<=c[i][0]:
        ans+=1
        right=c[i][1]
print(ans)