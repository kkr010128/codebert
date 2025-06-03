import copy
 
H, W, K = map(int, input().split())
tiles = [list(input()) for _ in range(H)]
count  = 0
 
for num in range(2**(H+W)):
  copied_tiles = copy.deepcopy(tiles)
  for i in range(H+W):
    if num>>i&1:
      if i < H:
        for j in range(W):
          copied_tiles[i][j] = 'R'
      else:
        for j in range(H):
          copied_tiles[j][i-H] = 'R'
  black_c = 0
  for i in range(H):
    for j in range(W):
      if copied_tiles[i][j] == '#':
        black_c += 1
  if black_c == K:
    count += 1
print(count)