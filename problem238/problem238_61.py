
[N,K,S] = list(map(int,input().split()))

if S<10**9:
    dammy1 = [S]*K
    dammy2 = [S+1]*(N-K)
    out=dammy1 + dammy2

else:
    dammy1 = [S]*K
    dammy2 = [1]*(N-K)
    out=dammy1 + dammy2
print(*out)
