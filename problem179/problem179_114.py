n, m = map(int, input().split())
lst = [int(i) for i in input().split()]

s = 0
for i in range(n):
  s += lst[i]
count = 0
for i in range(n):
  if lst[i] * 4 * m >= s:
    count += 1
if count >= m:
  print('Yes')
else:
  print('No')