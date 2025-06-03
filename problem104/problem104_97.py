a,b,c=map(int,input().split())
if b%c==0 or a%c==0:
  print(int((b-a)/c)+1)
else:
  print(int((b-a)/c))