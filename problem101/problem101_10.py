a, b, c = map(int, input().split())
k = int(input())
n = 0

while a >= b:
  b = b*2
  n += 1
while b >= c:
  c = c*2
  n += 1

if a < b < c and n <= k:
  print('Yes')
else:
  print('No')