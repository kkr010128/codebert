N = input()
ans = 0
for i in range(3):
  if N[i] == '7':
    ans = 1
    break

if ans == 1:
  print('Yes')
else :
  print('No')
