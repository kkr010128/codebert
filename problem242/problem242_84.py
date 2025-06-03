N,K=map(int,input().split())
A=sorted(map(int,input().split()))

M=10**9+7

t,b=A[K-1]-A[N-K],1
for i in range(1,N-K+1):
  b=(b*(K-1+i)*pow(i,M-2,M))%M
  t=(t+b*(A[K-1+i]-A[N-K-i]))%M

print(t)
