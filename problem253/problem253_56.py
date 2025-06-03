n, a, b = map(int, input().split())
d = (b-a)//2
if (b-a) % 2:
  print(d + min(a, n-b+1))
else:
  print(d)