N,M=map(int,input().split())

pos=[]
for i in range(M):
    array=list(map(int,input().split()))
    pos.append(array)

flg=True
num=[-1 for i in range(N)]

for i in range(M):
    if num[pos[i][0]-1]==-1 or num[pos[i][0]-1]==pos[i][1]:
        if pos[i][0]-1!=0 or pos[i][1]!=0:
            num[pos[i][0]-1]=pos[i][1]
        else:
            if N==1:
                num[pos[i][0]-1]=pos[i][1]
            else:
                flg=False
    else:
        flg=False

for i in range(len(num)):
    if num[i]==-1:
        if i==0:
            if N==1:
                num[i]=0
            else:
                num[i]=1
        else:
            num[i]=0

ans=0
for i in range(N):
    ans+=num[i]*10**(N-i-1)

if flg:
    print(ans)
else:
    print("-1")