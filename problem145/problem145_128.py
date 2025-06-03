import collections

n,m = map(int,input().split())
g = [[] for i in range(n+1)]
for i in range(m):
  a,b = map(int,input().split())
  g[a].append(b)
  g[b].append(a)
q = collections.deque()
q.append(1)
check = [0]*(n+1)
check[1] = 1
ans = [0]*(n+1)
while len(q)!=0:
  v = q.popleft()
  for j in g[v]:
    if check[j] == 0:
      check[j] = 1
      ans[j] = v
      q.append(j)
print('Yes')
for k in range(2,n+1):
  print(ans[k])