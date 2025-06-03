n=int(input())
ans=0
for x in range(1,n+1):
  b=n//x
  c=x*b
  ans1=(x+c)*b//2
  ans+=ans1

print(ans)
