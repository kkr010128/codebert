n=int(input())
ans=0
m=1
while n>1:
  n=n//2
  ans+=m
  m*=2
print(ans+m)
