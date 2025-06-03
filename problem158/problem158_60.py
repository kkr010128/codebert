n=int(input())
j,k=map(int,input().split())
f=1
if k-j>=n:
  print('OK')
  f=0
else:
  for i in range(j,k+1):
    if i%n==0:
      print('OK')
      f=0
      break
if f==1:
  print("NG")