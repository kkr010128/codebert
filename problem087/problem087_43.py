N = input()
SUM = 0
for i in N:
  SUM += int(i)
if SUM % 9 == 0:
  print('Yes')
else :
  print('No')