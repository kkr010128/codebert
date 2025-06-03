n,k,s=map(int,input().split())
if s==1000000000:
  x=[s]*k+[1]*(n-k)
else:
  x=[s]*k+[s+1]*(n-k)
print(*x)