n=int(input())
ans=0
for a in range(1,n):
  x=(n-1)//a
  ans+=x
print(ans)
