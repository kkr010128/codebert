n, m=map(int, input().split())
x = list(map(int, input().split()))

y = sorted(x, reverse=True)
if y[m-1] >= sum(x)/(4*m):
  print('Yes')
else:
  print('No')