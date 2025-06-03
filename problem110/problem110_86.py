H,W,K=map(int,input().split())
c=[str(input())for i in range(H)]
ans=0
for maskH in range(2**H):
    for maskW in range(2**W):
        black=0
        for i in range(H):
            for j in range(W):
                if ((maskH>>i)&1)==1:
                    continue
                if ((maskW>>j)&1)==1:
                    continue
                if c[i][j]=='#':
                    black+=1
        if black==K:
            ans+=1
print(ans)