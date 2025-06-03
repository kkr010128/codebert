N,K=map(int,input().split())
a=N%K
b=abs(N%K-K)
print(min(a,b))