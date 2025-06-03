a,b,c=map(int,input().split())
k=int(input())
x=0
while a>=b:
  b=b*2
  x=x+1
while b>=c:
  c=c*2
  x=x+1
if k>=x:
  print('Yes')
else:
  print('No')