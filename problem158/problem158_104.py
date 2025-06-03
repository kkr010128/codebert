k = int(input())
a,b = map(int,input().split())

x = (b // k) * k

if a <= x <= b :
  print('OK')
else :
  print('NG')