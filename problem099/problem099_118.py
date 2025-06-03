import math

n, k = map(int,input().split())
list = [int(x) for x in input().split()]
list.sort()

l = 0
r = max(list)

while r - l > 1:
  count = 0
  x = (r + l)//2

  for i in range(len(list)):
    if x >= list[i]:
      continue
    count += math.ceil(list[i]/x) - 1

  if count <= k:
    r = x
  else:
    l = x

print(r)

