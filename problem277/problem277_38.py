H,W,K=map(int, input().split())
S=[input()for _ in range(H)]
A=[[0]*W for _ in range(H)]
c=0
for i in range(H):
    d=0
    for j in range(W):
        if S[i][j]=="#":
            c+=1
            d=c
        A[i][j]=d
    p=0
    for j in range(W-1,-1,-1):
        if A[i][j]==0:
            A[i][j]=p
        p=A[i][j]
    if S[i].find("#")<0 and i!=0:
        A[i][:]=A[i-1]
for i in range(H-2,-1,-1):
    if all(a==0 for a in A[i]):
        A[i][:]=A[i+1]
for i in range(H):
    print(*A[i])