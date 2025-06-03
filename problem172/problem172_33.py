n = str(input())
flag = 0
for i in range(3):
  if n[i] == '7':
    flag = 1

if flag == 1:
  print('Yes')
else:
  print('No')