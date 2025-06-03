a = [list(map(int, input().split())) for _ in range(3)]
n = int(input())
for _ in range(n):
  d = int(input())
  for i in range(3):
    if d in a[i]:
      a[i][a[i].index(d)] = -1

for i in range(3):
  if sum(a[i])==-3:
    print('Yes')
    exit()
  s = 0
  for j in range(3):
    s += a[j][i]
  if s==-3:
    print('Yes')
    exit()
if a[0][0]+a[1][1]+a[2][2]==-3:
  print('Yes')
  exit()
if a[0][2]+a[1][1]+a[2][0]==-3:
  print('Yes')
  exit()

print('No')