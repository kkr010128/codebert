tp,tf,ap,af = map(int,input().split())

from math import ceil
takahashi = ceil(tp/af)
aoki = ceil(ap/tf)

if takahashi >= aoki :
  print('Yes')
else :
  print('No')