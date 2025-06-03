n,m=map(int,input().split())
a=list(map(int,input().split()))

h=sum(a)

if n<h:
  print('-1')
else:
  print(n-h)