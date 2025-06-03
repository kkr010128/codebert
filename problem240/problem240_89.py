N,M=map(int,input().split())

AC=[0]*(N+1)
WA=[0]*(N+1)
ans=0
for _ in range(M):
    p,s=input().split()
    p=int(p)
    if AC[p]==0:
       if s=='AC':
            AC[p]=1
            ans+=WA[p]
       else:
            WA[p]+=1
print(sum(AC),ans)
