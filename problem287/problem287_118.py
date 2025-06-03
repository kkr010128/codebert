a = 0
N = int(input())
for i in range(1, 10):
  for j in range(1, 10):
    if N == i*j:
      print('Yes')
      a = 1
  if a == 1:
    break
if a == 0:
  print('No')