K,N=map(int, input().split())
A=list(map(int, input().split()))

B=[0]*N

for i in range(N-1):
    B[i]=A[i+1]-A[i]

B[-1]=A[0]+K-A[-1]

B=sorted(B)

ans = sum(B[0:-1])
print(ans)