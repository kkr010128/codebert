n,m=map(int,input().split())
l=[[] for _ in range(n)]
for i in range(m):
  a,b=map(int,input().split())
  l[a-1].append(b-1)
  l[b-1].append(a-1)
queue=[0]
visit=[0]*n
visit[0]=1
ans=[0]*n

while len(queue)>0: 
  now=queue.pop(0)
  for p in l[now]:
    if visit[p]==0:
      visit[p]+=1
      queue.append(p)
      ans[p]=now+1
k=ans[1:]
if not all(kk!=0 for kk in k):
  print('No')
  exit()
print('Yes')
for kk in k:
  print(kk)