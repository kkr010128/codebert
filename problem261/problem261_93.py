S=list(input())
N=len(S)
ans=0
for i in range(N):
    if S[i]!=S[-i-1]:
        ans+=1
print(int(ans/2))