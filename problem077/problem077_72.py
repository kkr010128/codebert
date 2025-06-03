a,b,c,d = map(int,input().split())
if(a<=0 and b>=0 or (c<=0 and d>=0)):
  print(max(a*c,b*d,a*d,b*c,0))
else:
  print(max(a*c,b*d,a*d,b*c))