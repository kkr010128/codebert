N = int(input())
 
numss = [[0]*(10) for _ in range(10)]

for i in range(1, N+1):
  ss = str(i)
  hd = int(ss[0])
  tl = int(ss[-1])
  numss[hd][tl] += 1
  #print(f'hd = {hd}, tl = {tl}')
  
ans = 0
for x in range(1, 10):
  for y in range(1, 10):
    ans += numss[x][y] * numss[y][x]

print(ans)