X,Y=map(int,input().split())

prize=[0,300000,200000,100000]

ans=0
for c in [X,Y]:
    if c<=3:
        ans+=prize[c]

if X==Y==1:
    ans+=400000

print(ans)