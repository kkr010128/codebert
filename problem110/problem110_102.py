import copy
 
H, W, K = map(int, input().split())
tiles = [list(input()) for _ in range(H)]
answer  = 0

for h in range(2**H):
  for w in range(2**W):
    b_cnt = 0
    for i in range(H):
      for j in range(W):
        if not (h>>i&1 or w>>j&1) and tiles[i][j] == '#':
          b_cnt += 1
    if b_cnt == K:
      answer += 1
print(answer)