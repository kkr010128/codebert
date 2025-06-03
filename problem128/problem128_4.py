x, n = list(map(int, input().split()))

if n == 0:
  print(x)
  exit(0)
else:
  arr = list(map(int, input().split()))

arr.sort()
if x in arr:
  i = arr.index(x)
else:
  print(x)
  exit(0)

if not i and i != 0:
  print(x)
  exit(0)

j = 1
for _ in range(n):
  row = i - j
  high = i + j
  if x - j not in arr:
    print(x - j)
    exit(0)
  elif x + j not in arr:
    print(x + j)
    exit(0)
  j += 1

print(x-1)
