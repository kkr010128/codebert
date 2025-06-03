a,b=(map(int,input().split()))
c=0
if a<=b:
  print(0)
elif a>b:
  c=a-b*2
  if c>0:
    print(c)
  elif c<=0:
    print(0)