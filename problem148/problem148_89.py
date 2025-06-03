a,b,c,k = map(int,input().split())
 
if k < a:
  print(str(k))
elif k < (a + b):
  print(str(a))
else:
  print(str(2*a + b - k))