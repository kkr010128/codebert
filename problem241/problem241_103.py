from collections import deque
h,w=map(int,input().split())
s=[list(input()) for _ in range(h)]
check=[[0,-1],[0,1],[-1,0],[1,0]]
ans=0
for i in range(h):
    for j in range(w):
        if s[i][j]==".":
            d = deque()
            d.append([i,j])
            a = [[-1] * w for _ in range(h)]
            a[i][j]=0
            while d:
                v = d.popleft()
                ii=v[0]
                jj=v[1]
                for c in check:
                    x=c[0]
                    y=c[1]
                    if ii+x in range(h) and jj+y in range(w):
                        if a[ii+x][jj+y]==-1:
                            if s[ii+x][jj+y]==".":
                                a[ii+x][jj+y]=a[ii][jj]+1
                                d.append([ii+x,jj+y])
                            else:
                                a[ii+x][jj+y]=0
            ans2=sorted(sum(a,[]),reverse=True)[0]
            if ans<ans2:
                ans=ans2
print(ans)