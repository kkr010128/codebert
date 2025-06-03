S=input()
N=len(S)

count=[0]*(N+1)
i=0
while i<N:
    if S[i]=='<':
        count[i+1]=count[i]+1
    i+=1

S=S[::-1]
count=count[::-1]
i=0
while i<N:
    if S[i]=='>':
        count[i+1]=max(count[i+1],count[i]+1)
    i+=1

print(sum(count))