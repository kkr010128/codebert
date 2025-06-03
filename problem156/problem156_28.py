from collections import defaultdict

d = defaultdict(list)
for i in range(-120, 121):
  for j in range(-120, 121):
    x = i**5 - j**5
    if x >= 1:
      d[x] = [i, j]
    
X = int(input())

print('{0[0]} {0[1]}'.format(d[X]))