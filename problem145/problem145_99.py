from collections import deque
n,m=map(int,input().split())
data=[[] for i in range(n+1)]
for i in range(m):
  a,b=map(int,input().split())
  data[a].append(b)
  data[b].append(a)
que=deque()
que.append(1)
cnt=[0]*(n+1)
while que:
  h=que.popleft()
  for u in data[h]:
    if cnt[u]!=0:
      continue
    cnt[u]=h
    que.append(u)
print('Yes')
for i in range(2,n+1):
  print(cnt[i])