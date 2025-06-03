N=int(input())
LR=[]
for i in range(N):
    X,L=map(int,input().split())
    LR.append([X-L,X+L])
LR.sort(key=lambda x:x[1])
nin=LR[0][1]
ans=1
for i in range(1,N):
    if nin<=LR[i][0]:
        nin=LR[i][1]
        ans+=1

print(ans)