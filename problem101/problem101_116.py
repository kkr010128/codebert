a, b, c = map(int, input().split())
k = int(input())
while a >= b and k > 0:
  b = b*2
  k = k-1
while b >= c and k > 0:
  c = c*2
  k = k-1
if a < b < c:
  print('Yes')
else:
  print('No')