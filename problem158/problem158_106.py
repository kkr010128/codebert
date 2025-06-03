k = int(input())
a , b = map(int,input().split())
if a//k != b//k or (b%k)*(a%k) == 0:
  print('OK')
else:
  print('NG')