number=list(map(int,input().split()))
H,W,K=number[0],number[1],number[2]
masu=[]
for i in range(H):
    tmp=list(str(input()))
    masu.append(tmp)
count=0
ans=0
for cowmask in range(1<<H):
    for rowmask in range(1<<W):
        count=0
        for x in range(H):
            for y in range(W):
                if (cowmask>>x)&1==0 and (rowmask>>y)&1==0 and masu[x][y]=="#":
                    count+=1
        if count==K:
            ans+=1
print(ans)