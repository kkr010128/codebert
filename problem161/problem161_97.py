a,b,n=map(int,input().split())

if n<b:
  c=(a*n)//b
  print(c)
  
else:
  c=(a*(b-1))//b
  print(c)