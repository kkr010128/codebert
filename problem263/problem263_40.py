p0 = 10**9+7
def pow(x,m):
    if m==0:
        return 1
    if m==1:
        return x
    if m%2==0:
        return (pow(x,m//2)**2)%p0
    else:
        return (x*(pow(x,(m-1)//2)**2)%p0)%p0

N = int(input())
A = list(map(int,input().split()))
A = [bin(A[i])[2:] for i in range(N)]
A = ["0"*(60-len(A[i]))+A[i] for i in range(N)]
C = {k:0 for k in range(60)}
for i in range(N):
    for m in range(60):
        if A[i][m]=="1":
            C[59-m] += 1
B = [0 for _ in range(60)]
for k in range(60):
    p = C[k]
    m = N-C[k]
    B[k] = p*m
cnt = 0
for k in range(60):
    cnt = (cnt+B[k]*pow(2,k))%p0
print(cnt)