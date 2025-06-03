a, b, c, d = map(int, input().split())

flg = False
while True:
  if c - b <= 0:
    flg = True
    break
  
  if a - d <= 0:
    flg = False
    break
  
  a -= d
  c -= b
  
print('Yes' if flg else 'No')