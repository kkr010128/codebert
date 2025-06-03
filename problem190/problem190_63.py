S = list(input())
N = len(S)

S_1=S[:N//2]
S_2=S[N//2+1:]

N_=len(S_1)
ans='Yes'
for n in range(N_):
    if S_1[n] != S_1[-(n+1)]:
        ans='No'
        break
    if S_2[n] != S_2[-(n+1)]:
        ans='No'
        break   
        
for n in range(N):
    if S[n] != S[-(n+1)]:
        ans='No'
        break

print(ans)