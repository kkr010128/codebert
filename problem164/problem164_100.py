a,b,c,d=map(int,input().split())
for i in range(1001):
  if i%2==0:
    c-=b
    if c<=0:
      print("Yes")
      exit(0)
  else:
    a-=d
    if a<=0:
      print("No")
      exit(0)
