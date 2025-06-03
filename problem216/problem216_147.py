A = list(map(int, input().split()))
L = []
for i in A:
  if i not in L:
    L.append(i)
if len(L) == 2:
  print('Yes')
else:
  print('No')