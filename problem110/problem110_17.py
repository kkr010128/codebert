def main2():
    h,w,k = map(int,input().split()) 
    G = []
    for _ in range(h):
        c = list(input())
        G.append(c)
    ans = 0

    for ib in range(1<<h):
        for jb in range(1<<w):
            ct = 0
            for i in range(h):
                for j in range(w):
                    if (ib>>i)&1 and (jb>>j)&1 and G[i][j]=="#":
                        ct+=1
            
            if ct == k:
                ans+=1
    
    print(ans)
main2()