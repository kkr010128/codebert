h,w,k=map(int,input().split())
c=list(list(input()) for _ in range(h))
ans=0
for n in range(2**(h+w)):
    l={}
    o={}
    x=0
    for m in range(h+w):
        if (n>>m)&1:
            if m>=h:
                o[m-h]=1
            else:
                l[m]=1
    for i in range(h):
        if not i in l:
            for j in range(w):
                if not j in o:
                    if c[i][j]=="#":
                        x+=1
    if x==k:
        ans+=1
print(ans)
