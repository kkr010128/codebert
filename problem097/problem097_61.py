k = int(input())
start = 7
if k % 2 == 0:
  print("-1")
  exit()
for i in range(k + 1):
  if start % k == 0:
    print(i + 1)
    exit()
  start = (start * 10 + 7) % k
print("-1")