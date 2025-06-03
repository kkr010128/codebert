x, n = [int(i) for i in input().split()]
a = [int(i) for i in input().split()] if n != 0 else []
min_ = 100
cnt = 0
for i in range(100 + 2):
  if abs(i - x) < min_ and not i in a:
    min_ = abs(i - x)
    cnt = i
print(cnt)