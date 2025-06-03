n, m = map(int,input().split())
if (n < 2):
  a = 0
else:
  a = int(n*(n - 1)/2)
if (m < 2):
  b = 0
else:
  b = int(m*(m - 1)/2)
print(a + b)
