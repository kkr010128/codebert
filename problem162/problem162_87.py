n, m = map(int, input().split())
if m%2 == 0:
  x = m//2
  y = m//2
else:
  x = m//2
  y = m//2+1
for i in range(x):
  print(i+1, 2*x+1-i)
for i in range(y):
  print(i+2*x+2, 2*y+2*x+1-i)