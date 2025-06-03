#E
H,W,K = map(int,input().split())
S = [list(str(input())) for _ in range(H)]
inf = float("inf")

ans = inf
T = 2**(H-1)
for i in range(T):
    b = bin(i)
    b = b.lstrip("0b")
    blist = list(b)
    lb = len(b)
    clist = blist[::-1]
    while lb < H-1:
        clist.append("0")
        lb+=1
    
    r = clist.count("1")
    count = r
    nw = [0]*(r+1)
    for w in range(W):
        nind = 0
        for h in range(H):
            if h > 0:
                if clist[h-1] == "1":
                    nind+=1

            if S[h][w] == "1":
                nw[nind]+=1
        
        if w == 0:
            pass
        else:
            for k in nw:
                if k > K:
                    count+=1
                    nw = [0]*(r+1)
                    
                    nind = 0
                    for h in range(H):
                        if h > 0:
                            if clist[h-1] == "1":
                                nind+=1

                        if S[h][w] == "1":
                            nw[nind]+=1
                    
                    if max(nw) > K:
                        count = inf
                    
                    break
    
    ans = min(ans,count)
    
print(ans)
        
        
        
    




