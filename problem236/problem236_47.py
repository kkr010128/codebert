row = int(input())
colmun = int(input())
top = int(input())
low, high = 0,0
if row <= colmun:
  low, high = row, colmun
else:
  low, high = colmun, row
for n in range(low):
  if (n + 1) * high >= top:
    print(n + 1)
    break