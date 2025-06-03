N=int(input())
ans=float("inf")
i=1
while i**2<=N:
  if N%i==0:
    temp=(i-1)+(N//i -1)
    ans=min(ans, temp)
  i+=1
print(ans)