n=int(input())
a=[]

for i in range(1,10):
  for j in range(1,10):
    a.append(i*j)
else:
  if n in a:
    print('Yes')
  else:
    print('No')