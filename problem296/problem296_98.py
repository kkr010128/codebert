S=input()
K=int(input())
N=len(S)
ans=None
if len(set(S))==1:
    ans=N*K//2
else:
    li=[]
    i=0
    while(i<N):
        j=i
        c=S[i]
        cnt=0
        while(j<N and c==S[j]):
            cnt+=1
            j+=1
        li.append((c,cnt))
        i=j
    res=0
    if li[0][0]!=li[-1][0]:
        for x,y in li:
            res+=y//2
        ans=res*K
    else:
        for i in range(1,len(li)-1):
            res+=li[i][1]//2
        ans=res*K+li[0][1]//2+li[-1][1]//2+(li[0][1]+li[-1][1])//2*(K-1)
print(ans)