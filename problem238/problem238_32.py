N,K,S = map(int,input().split())

cur = 1 if S==10**9 else S+1

ans = [S]*K +[cur]*(N-K)

print(*ans)
