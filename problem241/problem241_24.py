import copy
h, w = map(int,input().split())

maze = [[9]*(w+2)]
for i in range(h):
  s = input()
  tmp = [9]
  for j in s:
    if j == "#":
      tmp.append(9)
    else:
      tmp.append(0)
  tmp.append(9)
  maze.append(tmp)
maze.append([9]*(w+2))
#print(maze)

def bfs(start):
  maze2 = copy.deepcopy(maze)
  #print(maze2)
  pos = [start]
  max_depth = 0
  maze2[start[0]][start[1]] = 2
  while len(pos):
    x, y, depth = pos.pop(0)
    max_depth = max(depth, max_depth)
    
    if maze2[x-1][y] < 2:
      pos.append([x-1,y,depth + 1])
      maze2[x-1][y] = 2
    if maze2[x+1][y] < 2:
      pos.append([x+1,y,depth + 1])
      maze2[x+1][y] = 2
    if maze2[x][y-1] < 2:
      pos.append([x,y-1,depth +1])
      maze2[x][y-1] = 2
    if maze2[x][y+1] < 2:
      pos.append([x,y+1,depth +1])
      maze2[x][y+1] = 2
  return max_depth

ans = 0
for i in range(h):
  for j in range(w):
      start = [i+1,j+1,0]
      maze2 = maze
      if maze[i+1][j+1] != 9:
        #print(bfs(start))
        ans = max(ans,bfs(start))
print(ans)