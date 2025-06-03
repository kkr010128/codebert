from collections import deque

H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]

dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]

dist = [[-1] * W for _ in range(H)]

def BFS(y, x):
  """(y, x)からはじめて、道のマスをBFSで最短距離を探す"""
  que = deque()
  que.append((y, x))
  dist[y][x] = 0
  max_dist = 0
  while que:
    sy, sx = que.popleft()  # popleft?
    for dy, dx in dir:
      ny = sy + dy
      nx = sx + dx
      if 0 <= ny < H and 0 <= nx < W and S[ny][nx] != "#" and dist[ny][nx] == -1:
        que.append((ny, nx))
        dist[ny][nx] = dist[sy][sx] + 1
        max_dist = max(max_dist, dist[ny][nx])
  
  return max_dist

max_dist = 0
for sy in range(H):
  for sx in range(W):
    if S[sy][sx] != "#":
      dist = [[-1] * W for _ in range(H)]
      max_dist = max(max_dist, BFS(sy, sx))

print(max_dist)