N,K,S=map(int,input().split())
ans=[S]*K+[[7,S+1][S!=10**9]]*(N-K)
print(*ans)