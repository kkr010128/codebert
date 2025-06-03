N = int(input())
digits = list(map(int,str(N)))
if sum(digits) % 9 == 0:
  print('Yes')
else:
  print('No')