import math
while True:
  n = int(input())
  if n == 0: break
  points = list(map(int, input().split()))
  mean = sum(points) / n
  s = 0
  for point in points:
    s += (point - mean) ** 2
  std = math.sqrt(s / n)
  print(std)