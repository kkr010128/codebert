n, m = (int(i) for i in input().split())
tot = sum(int(i) for i in input().split())

if tot > n:
  print(-1)
else:
  print(n - tot)
