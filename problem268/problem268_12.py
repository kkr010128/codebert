n=int(input())
A=list(map(int,input().split()))
N=[3]+[0]*n
mod=10**9+7
ans=1

for a in A:
    ans*=N[a]
    ans%=mod
    N[a]-=1
    N[a+1]+=1
print(ans)