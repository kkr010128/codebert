N=int(input())
ans=(N*(N+1))//2  #1の時
for i in range(2,N+1):
  m=N//i
  ans+=i*(m*(m+1)//2)
print(ans)