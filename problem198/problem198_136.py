n=int(input())
l=[['a1']]+[[] for _ in range(9)]
for i in range(9):
  for b in l[i]:
    t=b[-1]
    for p in range(int(t)):
      l[i+1].append(b[:-1]+chr(97+p)+t)
    l[i+1].append(b[:-1]+chr(97+int(t))+str(int(t)+1))
for i in l[n-1]:
  if len(i)==12:
    print(i[:-2])
  else:
    print(i[:-1])