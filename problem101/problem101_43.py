a,b,c=map(int,input().split())
k=int(input())

f=False
for _ in range(k):
  if b<=a:
    b*=2
  elif c<=b:
    c*=2
  if c>b>a:
    f=True
    break

if f:
  print('Yes')
else:
  print('No')