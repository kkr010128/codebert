N,K,S=list(map(int, input().split()))
L=[0]*N
L[:K]=[S]*K
if S==10**9:
  L[K:]=[1]*(N-K)
else:
  L[K:]=[10**9]*(N-K)
print(*L)