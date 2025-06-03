n,m=map(int,input().split())
if (n>0) and (m>0):
  print(int(n*(n-1)/2+m*(m-1)/2))
else:
  print(int(max(n,m)*(max(n,m)-1)/2))