def colorchange(i,l,r,col):
    k=i-1
    while(k>=0):
        if not '#' in G[k]:
            for j in range(l+1,r+1):
                A[k][j]=col
        else:
            break
        k-=1
    k=i+1
    while(k<H):
        if not '#' in G[k]:
            for j in range(l+1,r+1):
                A[k][j]=col
        else:
            break
        k+=1
        

H,W,K=map(int,input().split())
G=[list(input()) for i in range(H)]
s=set()
A=[[-1]*W for i in range(H)]
now=1
for i in range(H):
    if not '#' in G[i]:
        continue
    last=-1
    first=True
    for j in range(W):
        if G[i][j]=='#' and j==0:
            first=False
        A[i][j]=now
        if j==W-1:
            colorchange(i,last,j,now)
            now+=1
        elif G[i][j+1]=='#':
            if first:
                first=False
            else:
                colorchange(i,last,j,now)
                last=j
                now+=1
for i in range(H):
    print(*A[i])