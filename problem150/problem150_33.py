n,k=map(int,input().split())
a=list(map(int,input().split()))
visit=[0 for i in range(n)]
goal,loop=[],[]
now=0

while visit[now]!=2 :
    if visit[now]==0 :
        goal.append(now)
    else :
        loop.append(now)
    visit[now]+=1
    now=a[now]-1

if len(goal)>k :
    print(goal[k]+1)
else :
    res=len(goal)-len(loop)
    print(loop[(k-res)%len(loop)]+1)