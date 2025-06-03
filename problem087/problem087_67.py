s = input()
q = []
for i in s:
  q.append(int(i))
if sum(q)%9 == 0:
  print('Yes')
else:print('No')