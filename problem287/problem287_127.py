N = int(input())
Suji_check = False
for s in range(1,10):
  for t in range(1,10):
    if s*t == N:
      Suji_check = True
      break
if Suji_check:
  print('Yes')
else:
  print('No')