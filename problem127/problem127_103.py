x, y = map(int, input().split())

ans = 0

for i in range(0, x + 1):
  # i is the number of the crane
  rest = y - (2 * i)
  if rest / 4 == x - i:
    print('Yes')
    ans = 1
    break

if ans == 0:
  print('No')
