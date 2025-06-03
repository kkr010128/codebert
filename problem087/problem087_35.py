s = input()
N = [int(c) for c in s]
add = 0

for i in range(len(N)):
  num = N[i]
  add += num
if add % 9 == 0:
  print('Yes')
else:
  print('No')