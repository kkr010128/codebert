x, y = map(int, input().split())

ans = 0
for i in [x, y]:
  if i <= 3:
    ans += 4 - i

if x == 1 and y == 1:
  ans += 4

print(ans * 100000)