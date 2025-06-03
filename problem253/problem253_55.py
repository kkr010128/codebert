N,A,B=map(int,input().split())
ans=min(A-1,N-B)+1+(B-A-1)//2
sum=0
if (B-A)%2==0:
    sum=(B-A)//2
    ans=min(sum,ans)
print(ans)