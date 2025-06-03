N, K = map(int, input().split())
S = 0
for p in range(K, N+2):
  S += p*(2*N-p+1)//2-p*(p-1)//2+1
  S %= 10**9+7
print(S)