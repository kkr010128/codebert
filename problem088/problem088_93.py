N=int(input())
*A,=map(int,input().split())

ans=0
p=A[0]
for i in range(1,N):
    if A[i]<p:
        ans+=p-A[i]
    else:
        p=A[i]
print(ans)