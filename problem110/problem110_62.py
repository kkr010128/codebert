import copy
H,W,K=map(int,input().split())
L=[[x for x in input()] for i in range(H)]
ans=0
for i in range(2**H):
    for j in range(2**W):
        C=copy.deepcopy(L)
        for k in range(H):
            if (i>>k&1):
                C[k]=["r"]*W
        for l in range(W):
            if (j>>l&1):
                for m in range(H):
                    C[m][l]="r"
        count=0
        for p in range(H):
            for q in range(W):
                if C[p][q]=="#":
                    count+=1
        if count==K:
            ans+=1
print(ans)
