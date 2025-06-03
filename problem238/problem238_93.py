N,K,S=map(int, input().split())
MAX = 10**9
if S != MAX:
    ans = [S]*K + [S+1]*(N-K)
    print(*ans)
else:
    ans = [S]*K + [S-1]*(N-K)
    print(*ans)