N=int(input())
S,T=input().split()
ans=S[0]+T[0]
for i in range(1,N):
    ans=ans+S[i]+T[i]
print(ans)