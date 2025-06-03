k = int(input())
a,b = map(int, input().split())

ct = 0
for i in range(a, (b+1)):
  if i % k == 0:
    ct += 1

if ct != 0:
  print('OK')
else:
  print('NG')