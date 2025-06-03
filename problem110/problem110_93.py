h,w,p=map(int,input().split())
A=[]
ans=0

for i in range(h):
    A.append(list(input()))

for i in range(2**h):
    hs=[False]*h
    for j in range(h):
        if ((i>>j)&1):
            hs[j]=True
    for k in range(2**w):
        ws=[False]*w
        for l in range(w):
            if ((k>>l)&1):
                ws[l]=True
        cnt=0
        for a in range(h):
            if hs[a]==True:
                for b in range(w):
                    if ws[b]==True:
                        if A[a][b]=='#':
                            cnt+=1
        if cnt==p:
            ans+=1
print(ans)