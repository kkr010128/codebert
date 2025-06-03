h = int(input())
w = int(input())
n = int(input())
cnt = 0
blk = 0

if h > w:
  for i in range(w):
    blk += h
    cnt += 1
    if blk >= n:
      break
else:
  for j in range(h):
    blk += w
    cnt += 1
    if blk >= n:
      break

print(cnt)