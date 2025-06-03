N=int(input())
A=list(map(int, input().split()))
A.append(0)
L=[0]*N
L[0]=1000

# dpしろ

for i in range(1,N):
    B=[0]*(i+1)
    for j in range(i):
        t=L[j]//A[j]
        B[j]=L[j]%A[j] + t*A[i]
    B[i]=L[i-1]
    L[i]=max(B)
print(L[N-1])