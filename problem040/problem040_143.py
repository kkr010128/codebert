a,b,c=map(int,input().split())
if a>b:
  n=a
  a=b
  b=n
else:
  pass
if b>c:
  n=b
  b=c
  c=n
else:
  pass
if a>b:
  n=a
  a=b
  b=n
else:
  pass
print(a,b,c)
