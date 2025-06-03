N, K, S = map(int, input().split())
S2 = S-1 if S == 1000000000 else S+1
As = [S]*K+[S2]*(N-K)
print(" ".join(map(str, As)))
