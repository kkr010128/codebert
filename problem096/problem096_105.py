n, d = [int(i) for i in input().split()]
cnt = 0
for _ in range(n):
  x, y = [int(i) for i in input().split()]
  if x**2 + y**2 <= d**2:
    cnt += 1
print(cnt)