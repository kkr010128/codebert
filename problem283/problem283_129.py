from math import ceil, floor
N = int(input())
half = floor(N / 2)
count = 0
for i in range(half):
  count = count + 1
if N % 2 != 0:
  print(count)
else:
  print(count - 1)