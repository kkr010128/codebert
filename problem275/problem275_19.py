xy = list(map(int,input().split()))
prise = 0

for i in xy:
  if i == 1:
    prise += 300000
  elif i == 2:
    prise += 200000
  elif i == 3:
    prise += 100000

if sum(xy) == 2:
  prise += 400000

print(prise)