N = int(input())
inf = 10 ** 6
graph = [[] for i in range(N)]
visited = [0 for i in range(N)]
time = [[inf,inf] for i in range(N)]

for i in range(N):
  a = list(map(int,input().split()))
  a = list(map(lambda x: x - 1,a))
  k,n = a[0],a[1]
  if n >= 0:
    graph[k] = a[2:]

con = 0

def dfs(cur,par):
  #print("v",visited)
  global con
  visited[cur] = 1
  con += 1
  time[cur][0] = min(time[cur][0],con)
  #print("cur1,con1",cur,con)
  if (graph[cur] == [] or graph[cur] == [cur]):
    visited[cur] = 1
    time[cur][0] = min(con,time[cur][0])
    con += 1
    time[cur][1] = min(con,time[cur][1])
    #print("curif,conif",cur,con)
    return 
  else:
    for chi in graph[cur]:
      if visited[chi] == 0:
        dfs(chi,cur)
      if any(visited[i] == 0 for i in graph[cur]):
        continue
      else:
        con += 1
        time[cur][1] = min(con,time[cur][1])
        #print("cur2,con2",cur,con)
        return
dfs(0,-1)

if any([i == 0 for i in visited]):
  f = visited.index(0)
  dfs(f,f - 1)

for i,t in enumerate(time):
  print(i + 1 ,*t)
