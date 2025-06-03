from sys import stdin



test = list(stdin.readline().rstrip())
 
result=0
 
for i in test:
  result = result + int(i)
 
if (result % 9) == 0:
  print('Yes')
else:
  print('No')
