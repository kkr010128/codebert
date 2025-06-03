a = int(input())
b = list(map(int, input().split()))
b = sorted(b)
c = b[0]
if c == 0:
  print(c)
  exit()
else:
  for i in range(a-1):
    c *= b[i+1]
    if c > 1000000000000000000:
      break

if c > 1000000000000000000:
  print(-1)
else:
  print(c)