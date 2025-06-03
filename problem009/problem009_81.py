from collections import deque
n=int(input())
l=[list(map(int,input().split())) for i in range(n)]
d=deque()
d.append(1)
check=[0]*n
check[0]=1
ans=[0]*n
kyori=[0]*n
while len(d)!=0:
  v=d.popleft()
  for i in l[v-1][2:]:
    if check[i-1]==0:
      check[i-1]=1
      ans[i-1]=(kyori[v-1]+1)
      kyori[i-1]=(kyori[v-1]+1)
      d.append(i)
for i in range(1,n):
  if ans[i]==0:
    ans[i]=-1
for i in range(n):
    print(i+1,ans[i])
