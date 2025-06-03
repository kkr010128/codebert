while 1:
  n,m=map(int,input().split())
  if n==0 and m==0:
    break
  if n<m:
    print(n,m)
  else:
    print(m,n)
