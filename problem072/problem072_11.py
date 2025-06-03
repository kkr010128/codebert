n = int(input())
total = 0

for i in range(n):
  a,b = map(int, input().split())
  if a == b:
    total += 1
    if total == 3:
      break
  else:
    total = 0
if total == 3:
  print('Yes')
else:
  print('No')