S=input()
T=input()

len_s=len(S)
len_t=len(T)

ans=0
for i in range(len_s-len_t+1):
    cnt=0
    for j in range(len_t):
        if S[i+j]==T[j]:
            cnt += 1
    ans = max(ans,cnt)
    
print(len_t-ans)