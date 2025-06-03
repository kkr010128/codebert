n = str(input())
s = 0
for x in n:
  s += int(x)
if s % 9 == 0:
  print('Yes')
else :
  print('No')