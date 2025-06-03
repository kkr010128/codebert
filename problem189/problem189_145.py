n, m = map(int, input().split())
c = 0
if n >= 2:
  c += n*(n-1) /2
if m >= 2:
  c += m*(m-1) /2
print(int(c))