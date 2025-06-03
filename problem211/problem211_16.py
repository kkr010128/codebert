n, m = map(int, input().split(" "))

if n <= 9:
  print(m + (100 * (10 - n)))
else:
  print(m)