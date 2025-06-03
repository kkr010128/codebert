import sys

n = int(input())
a = dict()
for x in map(int, input().split()):
  if a.get(x) == 1:
    print('NO')
    sys.exit()

  a[x] = 1

print('YES')
