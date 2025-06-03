n, x = int(input()), list(map(int, input().split()))
px = 0
a = 100 ** 100
for i in range(100):
  s = 0
  for j in x:
    s += (i-j) ** 2
  if a > s:
    a = s
print(a)