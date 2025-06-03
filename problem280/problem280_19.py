N = int(input())
cities = []
for n in range(N):
  cities.append(tuple(map(int, input().split())))

import math
def distance(i, j):
  xi,yi = cities[i]
  xj,yj = cities[j]
  xd,yd = xi - xj, yi - yj
  return math.sqrt(xd * xd + yd * yd)

# path: これまでに通過した街の番号
def search(path):
  total = 0
  count = 0
  for i in range(N):
    if i not in path:
      count += 1
      path.append(i)
      total += (0 if len(path) == 1 else distance(i, path[-2])) + search(path)
      path.remove(i)
  if count == 0:
    return 0
  else:
    return total / count

print(search([]))