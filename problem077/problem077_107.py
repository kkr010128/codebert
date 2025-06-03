a,b,c,d=map(int,input().split())
x=a*c
if x<a*d:
  x=a*d
if x<b*c:
  x=b*c
if x<b*d:
  x=b*d
print(x)