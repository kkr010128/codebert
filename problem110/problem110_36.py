# ABC_173_C_H_and_V.py

H,W,K=list(map(int, input().split()))
A=[list(input()) for _ in range(H)]
# print(A)

# bitDP2回ぶん回せば行けるのでは？
# bitが1は残す方で

ans=0
for i in range(1,2**H):
    for j in range(1,2**W):
        resx=[]
        resy=[]
        ct=0
        for k in range(H):
            if (i>>k)&1:
                resx.append(k)
        for l in range(W):
            if (j>>l)&1:
                resy.append(l)
        # print(resx,resy)
        B=[[A[k][l] for l in resy] for k in resx]
        for k in range(len(resx)):
            ct+=B[k].count('#')
        # print(ct)
        if ct==K:
            ans+=1
print(ans)