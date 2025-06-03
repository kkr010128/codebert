N=int(input())
ans=0
for a in range(1,N):
    q,m=divmod(N,a)
    ans+=(N//a)-(m==0)
print(ans)