from collections import deque

def bfs(graph, n, s):
  visited = [0]*n # 移動回数を保持
  visited[s] = 1 # 部屋1の探索は完了としている
  q = deque([s]) # 探索用にdequeを設定し、初期位置としてs(0)を設定する
  while q:
    node = q.popleft() # 先頭から順番に実行
    for i in graph[node]: # 各部屋から行ける別の部屋を確認
      if not visited[i]: # 値が"0"の場合に処理を実行
        visited[i] = node + 1 # 部屋1からの移動回数を保持する
        q.append(i) # 移動先の部屋をqに格納し、探索を継続する
  return visited

n,m = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
  a,b = map(lambda x: int(x)-1, input().split())
  graph[a].append(b)
  graph[b].append(a)
  
visited = bfs(graph, n, 0)[1:] # 幅優先探索を行い、部屋1以外の結果を取得する
if all(visited):
  print("Yes")
  print(*visited, sep="\n") 
else:
  print("No")