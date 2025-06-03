H, W = map(int, input().split())
maze = [0] * H
for i in range(H):
  maze[i] = str(input())

ans = 0  
for i in range(H):#20
  for j in range(W):#20
    if maze[i][j] != "#":
      visited = [[float("inf")] * W for _ in range(H)]
      visited[i][j] = 0
      queue = [[i, j]]
      while queue:#400
        x, y = queue.pop()
        for p, q in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
          if (0 <= x + p < H) and (0 <= y + q < W):
            if (maze[x+p][y+q] !="#"):       
              if visited[x+p][y+q] > visited[x][y] + 1:
                queue.append([x+p, y+q])
                visited[x+p][y+q] = visited[x][y] + 1
      #print(visited)        
      now = 0
      for k in range(H):
        for k2 in range(W):
          if visited[k][k2] < 10 ** 10:
            now = max(now, visited[k][k2])
      ans = max(ans, now)
      
print(ans)

            
            
            
            
        
