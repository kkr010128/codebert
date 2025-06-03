from bisect import bisect_left as bl

H,W,K=map(int,input().split())
s=[input() for _ in range(H)]

a=[[0 for _ in range(W)] for _ in range(H)]
OK=[]
NG=[]

n=0
for h in range(H):
    if "#" in s[h]:
        OK.append(h)
        n+=1
        f=s[h].index("#")
        for w in range(W):
            if w>f and s[h][w]=="#":
                n+=1
            a[h][w]=n
    else:
        NG.append(h)

if len(NG)>0:
    for n in NG:
        if n>max(OK):
            ref=max(OK)
        else:
            ref=OK[bl(OK,n)]
        for w in range(W):
            a[n][w]=a[ref][w]
for A in a:
    print(*A)