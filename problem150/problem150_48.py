N,K=map(int,input().split())
A=list(map(int,input().split()))
B=[1]
C=["#"]*N
roop=False
for i in range(K):
    if C[B[i]-1]=="#":
        C[B[i]-1]="$"
    else:
        roop=True
        break
    B.append(A[B[i]-1])
if roop==True:
    f=B.index(B[i])
    T=i-f
    if T==0:
        print(B[f])
    else:
        r=(K-f)%T
        print(B[f+r])
else:
    print(B[K])
