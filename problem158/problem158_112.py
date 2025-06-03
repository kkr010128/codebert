k = int(input())
a,b = map(int,input().split())
ans = 0
for i in range(a//k,b//k+1):
  if a <= k * i <= b:
    ans = 1
if ans == 1:
  print('OK')
else:
  print('NG')