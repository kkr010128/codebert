N,K=map(int,input().split())
m=N//K
print(min(abs(N-m*K),abs(N-(m+1)*K)))