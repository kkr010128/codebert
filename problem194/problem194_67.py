# coding: utf-8
H, W = list(map(int, input().split()))
S = []
for _ in range(H):
    S.append(list(input()))

grid = [[0 for _ in range(W)] for _ in range(H)]

for h in range(1,H):
  if S[h-1][0] == '#' and S[h][0] == '.':
    grid[h][0] = grid[h-1][0] + 1
  else:
    grid[h][0] = grid[h-1][0]
    
for w in range(1,W):
  if S[0][w-1] == '#' and S[0][w] == '.':
    grid[0][w] = grid[0][w-1] + 1
  else:
    grid[0][w] = grid[0][w-1]
for w in range(1,W):
  for h in range(1,H):
    if S[h-1][w] == '#' and S[h][w] == '.':
      next_h = grid[h-1][w] + 1
    else:
      next_h = grid[h-1][w]      
    if S[h][w-1] == '#' and S[h][w] == '.':
      next_w = grid[h][w-1] + 1
    else:
      next_w = grid[h][w-1]
    grid[h][w] = min([next_w, next_h])
if S[H-1][W-1] == '#':
  grid[H-1][W-1] += 1
print(grid[H-1][W-1])