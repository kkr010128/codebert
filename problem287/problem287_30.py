N = int(input())
answer = 0
for i in range(1,10):
  for j in range(1,10):
    if N == i*j:
      answer = 1
      break
if answer == 1:
  print('Yes')
else:
  print('No')