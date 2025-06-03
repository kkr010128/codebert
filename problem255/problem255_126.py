N=int(input())
S,T=input().split()

ans=''

for i in range(N):
    ans += S[i]
    for j in range(N):
        if i==j:
            ans +=T[j]
        
print(ans)