h,w=map(int,input().split())
s=[]
for i in range(h):
    s.append(input())
    
dij=[-1,0,1,0,-1]
def update(i,j,x,d,q):
    if(d[i][j]!=-1):return
    d[i][j]=x
    q.append((i,j))

m=-1
for i in range(h):
    for j in range(w):
        if(s[i][j]=="#"):continue
        d=[[-1 for ii in range(w)] for jj in range(h)]
        q=[]
        update(i,j,0,d,q)
        while q:
            xy=q.pop(0)
            xx=xy[0]
            yy=xy[1]
            for k in range(4):
                ni=xx+dij[k]
                nj=yy+dij[k+1]
                if(ni<0 or ni>=h or nj<0 or nj>=w):continue
                if(s[ni][nj]=="#"):continue
                update(ni,nj,d[xx][yy]+1,d,q)
        for ii in range(h):
            for jj in range(w):
                m=max(d[ii][jj],m)
print(m)