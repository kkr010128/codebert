import math

N,K=map(int,input().split())


sum=0
for s in range(K,N+1):
    sum+=(s*(2*N-s+1))/2-(s*(s-1))/2+1
print(int(sum+1)%1000000007)