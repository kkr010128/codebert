from collections import deque
n,m=map(int,input().split())
road=[[] for i in range(n)]
flag=[0]*n
for i in range(m):
    a,b=map(int,input().split())
    road[a-1].append(b-1)
    road[b-1].append(a-1)
count=0
for i in range(n):
    if flag[i]!=0:
        continue
    count+=1
    q=deque([i])
    while q:
        p=q.popleft()
        flag[p]=1
        for z in road[p]:
            if flag[z]==0:
                q.append(z)
print(count-1)