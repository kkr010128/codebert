def g(x):
  return x*(x+1)//2
n=int(input())
ans=0
for i in range(1,n+1):
  ans=ans+i*g(n//i)
print(ans)