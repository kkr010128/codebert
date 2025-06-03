N=int(input())
S=input()
ans=0
for i in range(N-2):
    if S[i]=='A':
        i+=1
        if S[i]=='B':
            i+=1
            if S[i]=='C':
                ans+=1
print(ans)