N=int(input())
A=list(map(int,input().split()))
ans=20202020200
sum_A=0
sum_B=sum(A)
for i in range(N):
    sum_A+=A[i]
    sum_B-=A[i]
    tmp=abs(sum_A-sum_B)
    if tmp<ans:
        ans=tmp
print(ans)