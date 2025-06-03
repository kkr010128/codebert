A,B,C,D = [int(x) for x in input().split()]
if A % D == 0 :
  takahashi = A // D
else:
  takahashi = A // D + 1
if C % B == 0 :
  aoki = C // B
else:
  aoki = C // B + 1
if takahashi >= aoki:
  print('Yes')
else:
  print('No')