S=list(str(input()))
ans=0
sofar=0
j=1
nax=0
for i in range(len(S)-1):
    if S[i]==S[i+1]:
        ans+=j
        j+=1
    elif S[i]=='<' and S[i+1]=='>':
        ans+=j
        nax=j
        j=1    
    else:
        ans+=j
        if nax!=0:
            ans-=j
        j=1
        nax=0
    if j>nax:
        ans-=nax
        nax=0
if j>nax:
    ans+=j
    ans-=nax
print(ans)