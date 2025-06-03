ans=0
N=int(input())
for x in range(1,N+1):
  if x%3==0 or x%5==0:
    pass
  else:
    ans += x
print(ans)