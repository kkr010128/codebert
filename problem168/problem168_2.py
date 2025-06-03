n, m = map(int,input().split())
lst = list(map(int,input().split()))
x = 0
for i in range(m):
  x = x + lst[i]
if (x > n):
  print("-1")
else:
  print(n - x)