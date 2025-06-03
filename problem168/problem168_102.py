a = list(map(int, input().split()))
b = list(map(int, input().split()))
if a[0] - sum(b) >= 0:
  print(a[0] - sum(b))
else:
  print(-1)
