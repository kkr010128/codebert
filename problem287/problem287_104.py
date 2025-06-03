N = int(input())
kuku = []
for x in range(1,10):
  for y in range(1,10):
    kuku.append(x*y)
    
if N in kuku:
  print('Yes')
else:
  print('No')