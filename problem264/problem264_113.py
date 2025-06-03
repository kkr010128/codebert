li = []
for i in range(2):
  a,b = map(int, input().split())
  li.append(a)
  
if li[1] == li[0]+1:
  print(1)
else:
  print(0)