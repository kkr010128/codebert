import sys

x = []

for line in sys.stdin.readlines():
  x.append(line.strip())

max = -(10**9)
min = int(x[1])

for i in range(2, int(x[0])+1):
  sa = int(x[i]) - min
  if max < sa:
    max = sa
  if min > int(x[i]):
    min = int(x[i])

  

print max