H, W= map(int, input().split())
A=[]
b=[]
ans=[0 for i in range(H)]
for i in range(H):
    A.append(list(map(int, input().split())))
for j in range(W):
    b.append(int(input()))
for i in range(H):
    for j in range(W):
        ans[i]+=A[i][j]*b[j]
    print(ans[i])