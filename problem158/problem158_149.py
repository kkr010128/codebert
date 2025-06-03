x = int(input())
a, b = map(int, input().split())
ans=0
for i in range(a,b+1):
  if i%x==0:
    ans=1
    break
if ans==1:
  print('OK')
else:
  print('NG')