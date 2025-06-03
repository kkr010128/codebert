a,b,c,d=map(int,input().split())
if (b<0 and c>0) or (a>0 and d<0):
  print(max(a*c,a*d,b*c,b*d))
else:
  print(max(0,a*c,a*d,b*c,b*d))