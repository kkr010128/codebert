N=int(input())
S=input()
R=0;G=1;B=2
C=["R","G","B"]
X=[[[0 for i in range(N+1)]for x in range(2)] for c in range(3)]
for c in range(3):
    for i in range(N):
        if S[i]==C[c]:
            X[c][0][i+1]=X[c][0][i]+1
        else:
            X[c][0][i+1]=X[c][0][i]
    for i in range(N-1,-1,-1):
        if S[i]==C[c]:
            X[c][1][i]=X[c][1][i+1]+1
        else:
            X[c][1][i]=X[c][1][i+1]
ans=0
for i in range(N):
    c=-1
    for cc in range(3):
        if C[cc]==S[i]:
            c=cc
            break
    for seq in [((c+1)%3,(c+2)%3),((c+2)%3,(c+1)%3)]:
        x,y=seq
        ans+=X[x][0][i]*X[y][1][i]
for i in range(N):
    x=0
    while(i+2*x<N):
        j=i+x
        k=i+2*x
        if len({S[i],S[j],S[k]})==3:
            ans-=1
        x+=1
print(ans)
