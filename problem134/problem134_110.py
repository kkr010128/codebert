N=int(input())
A=list(map(int,input().split()))

ans=1

if A.count(0)>0:
    ans=0
for i in range(N):
    ans*=A[i]
    if ans>10**18:
        ans=-1
        break
print(ans)