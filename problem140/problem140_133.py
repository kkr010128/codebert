pd = list(input())


for i in range(len(pd)):
  if pd[i] == '?':
    pd[i] = 'D'


for s in pd:
  print(s, end=(""))
