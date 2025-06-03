n,u,v = map(int,input().split())
u -= 1
v -= 1
peer = [[] for _ in range(n)]
for _ in range(n-1):
  a,b = map(int,input().split())
  a -= 1
  b -= 1
  peer[a].append(b)
  peer[b].append(a)
rank = [10**6 for _ in range(n)]
seen = [0 for _ in range(n)]
pre = [10**6 for _ in range(n)]
pst = [[] for _ in range(n)]
seen[v] = 1
rank[v] = 0
now = [v]
while now:
  last = now
  now = []
  for x in last:
    for y in peer[x]:
      if seen[y] == 0:
        seen[y] += 1
        rank[y] = rank[x] + 1
        now.append(y)
        pre[y] = x
        pst[x].append(y)
#print(rank)
back = (rank[u]-1) // 2
tar = u
for _ in range(back):
  tar = pre[tar]
depth = -1
now = [tar]
while now:
  depth += 1
  last = now
  now = []
  for x in last:
    now += pst[x]
#print(tar,depth,last)
if rank[u] % 2 == 1:
  print(back + depth)
else:
  print(back + depth + 1)