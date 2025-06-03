r, g, b = list(map(int, input().split()))
k = int(input())
count = 0

while r >= g:
  g *= 2
  count += 1
  
while g >= b:
  b *= 2
  count += 1

if k >= count:
  print('Yes')
else:
  print('No')