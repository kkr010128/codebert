N,K = map(int,input().split())
P = list(map(int,input().split()))
A = [0 for _ in range(N)]
for i in range(N):
    A[i] = (P[i]+1)/2
cmax = sum(A[:K])
a = cmax
for i in range(1,N-K+1):
    a = a+A[i+K-1]-A[i-1]
    cmax = max(cmax,a)
print(cmax)