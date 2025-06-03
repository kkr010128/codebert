H,W,K = map(int,input().split())
s = [input() for i in range(H)]
a = [["."]*W for i in range(H)]
tag = 1
for h in range(H):
    l = 0
    for w in range(W):
        if s[h][w]=="#":
            a[h][l:w+1] = [tag]*(w+1-l)
            l = w+1
            tag+=1
    if l!=0 and l!=W:
        a[h][l-1:W] = [tag-1]*(W-l+1)
for h in range(H):
    for w in range(W):
        if a[h][w]==".":
            for k in range(h,H):
                if a[k][w]!=".":
                    a[h][w]=a[k][w]
                    break
            if a[h][w]==".":
                for k in range(h,-1,-1):
                    if a[k][w]!=".":
                        a[h][w]=a[k][w]
                        break
for b in a:print(*b)