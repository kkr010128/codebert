N, K, S = map(int,input().split())
if S != 10**9:
    A = [S]*K + [S+1]*(N-K)
else:
    A = [S]*K + [1]*(N-K)
print(*A)
