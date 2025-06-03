a,b,c=map(int,input().split())
k=int(input())
for i in range(1,k+1):
  if a>=b>=c or a>=c>=b:
    c=c*2
  elif b>=a>=c or b>=c>=a:
    c=c*2
  elif c>=b>a:
    c=c*2
  elif c>b==a:
    b=b*2
  elif c>a>=b:
    b=b*2
if c>b>a:
  print('Yes')
else:
  print('No')
