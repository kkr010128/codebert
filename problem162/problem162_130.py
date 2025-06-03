n,m=map(int,input().split())
for i in range(m):
  if n%2==0 and 2*m-i-i-1>=n//2:
    print(i+1,2*m-i+1)
  else:
    print(i+1,2*m-i)