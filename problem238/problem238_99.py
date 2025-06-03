N, K, S=map(int, input().split())
A=[str(S)]*K
if S==10**9:
  B=["1"]*(N-K)
else:
  B=[str(S+1)]*(N-K)
ans=A+B
print(" ".join(ans))
