N = int(input())
zoro_count = 0
zoro = False
for n in range(N):
  dn1,dn2 = map(int, input().split())
  if dn1 == dn2:
    zoro_count += 1
  else:
    zoro_count = 0
  if zoro_count >= 3:
    zoro = True
if zoro:
  print('Yes')
else:
  print('No')