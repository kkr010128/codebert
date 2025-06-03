from statistics import mean
import math
ans = []
while 1:
  n = int(input())
  if n == 0: break
  l = list(map(int, input().split()))
  m = mean(l)
  print("{0:.8f}".format(math.sqrt(sum([(s - m) ** 2 for s in l]) / n)))
