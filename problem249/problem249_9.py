a,b,k=map(int,input().split())

if a<=k:
  
  k-=a
  a=0
  
  if b<=k:
    print(0,0)
  else:
    b-=k
    print(a,b)

elif k<a:
  a-=k
  print(a,b)


