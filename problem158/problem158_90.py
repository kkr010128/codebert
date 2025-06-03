K = int(input())
A,B = map(int, input().split())
if B-A >= K-1:
  print('OK')
elif (B//K)*K >= A:
  print('OK')
else:
  print('NG')