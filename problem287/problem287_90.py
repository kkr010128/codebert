n = int(input())

a = False

for x in  range(1,10):
  for y in range(1,10):
    if x*y == n:
      print("Yes")
      a = True
      break
  if a:
    break

else:
  print("No")
