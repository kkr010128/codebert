X = int(input())
j = 2
for i in range(X,(X - 1) * 2):
  while i % j != 0 and j <= i:
    j += 1
  if j == i:
    print(i)
    break
  j = 2
if X == 2:
  print(2)