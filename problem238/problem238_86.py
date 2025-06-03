N,K,S=map(int,input().split())
if S==1:
    A=[S]*K+[S+1]*(N-K)
else:
    A = [S] * K + [S - 1] * (N - K)
print(*A)