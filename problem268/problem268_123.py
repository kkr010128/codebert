P=10**9+7
N=int(input())
A=list(map(int, input().split()))
ans=1
c=[0,0,0]
for i in range(N):
  a,f,k=A[i],-1,0
  for j in range(3):
    if c[j]==a:
      k+=1
      if f==-1:
        c[j]+=1
        f=j
  ans=(ans*k)%P
print(ans)