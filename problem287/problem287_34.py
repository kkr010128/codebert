N=int(input())
b=0
for x in range(1,10):
  for y in range(1,10):
    if x*y==N:
      b+=1
      break
  if b==1:
    break
if b==1:
  print("Yes")
else:
  print("No")