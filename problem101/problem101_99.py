a, b, c = map(int, input().split())
k = int(input())
flg = False
c = (2**k) * c
for i in range(k):
  if a < b < c:
    flg = True
    break
  b *= 2
  c //= 2

if flg:
  print('Yes')
else:
  print('No')
