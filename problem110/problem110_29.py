from copy import deepcopy

HEIGHT, WIDTH, K = map(int, input().split())
CELLS = [list(input()) for i in range(HEIGHT)]

ans = 0

for maskY in range(1<<HEIGHT):
  for maskX in range(1<<WIDTH):
    black=0
    for y in range(HEIGHT):
      for x in range(WIDTH):
        if (maskY >> y & 1) == 0 and (maskX >> x & 1) == 0 and CELLS[y][x] == '#':
          black+=1
    if K == black:
      ans+=1


print(ans)
