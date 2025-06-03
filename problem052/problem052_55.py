n = int(input())
i = 1
for i in range(1, n + 1):
 if i % 3 == 0:
  print(' {0}'.format(i), end = '')
 else:
  st = str(i)
  for x in range(0, len(st)):
   if st[x] == '3':
    print(' {0}'.format(i), end = '')
    break
print()