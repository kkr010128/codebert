N = int(input())
ans=0
for n in range(1, N+1):
  ans=ans if n%3==0 or n%5==0 else ans+n
print(ans)