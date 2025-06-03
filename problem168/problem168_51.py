a, b = map(int, input().split())
c = list(map(int, input().split()))
if a >= sum(c):
  print(a - sum(c))
else:
  print('-1')