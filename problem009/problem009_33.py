from collections import deque
N = int(input())
edge = [[] for _ in range(N+1)]
for i in range(N):
  A = list(map(int, input().split()))
  edge[A[0]] = A[2:]

ans = [-1]*N
ans[0] = 0
d = deque([[1,0]])
while len(d)>0:
  v,dist = d.popleft()
  for w in edge[v]:
    if ans[w-1]==-1:
      ans[w-1]=dist+1
      d.append([w,dist+1])
for i in range(N):
  print(i+1,ans[i])
