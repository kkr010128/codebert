N = int(input())
res = False
for i in range(1,10):
  for j in range(1,10):
    if i*j == N:
      res = True
      break
  if res:
    break

if res:
  print("Yes")
else:
  print("No")