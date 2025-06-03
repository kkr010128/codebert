N,K,S=map(int,input().split())
ans=[S]*K
if S==10**9:
    ans.extend([S-1]*(N-K))
else:
    ans.extend([S+1]*(N-K))
print(*ans)