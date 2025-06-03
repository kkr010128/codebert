nn = input()
n = str(input())

if len(n) % 2 == 1:
  print('No')
else:
  a = n[0 : len(n)//2]
  b = n[len(n)//2 : len(n)]
  if a == b:
    print('Yes')
  else:
    print('No')