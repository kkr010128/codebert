X = int(input())
lack = X % 1000
if lack == 0:
  print(0)
else:
  print(1000 - lack)