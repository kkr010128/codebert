n,m = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
if n >= sum(a):
  print(n - sum(a))
else:
  print(-1)