N,K = map(int, input().split())
N = N%K
while(abs(N-K) < N):
  N = abs(N-K)
print(N)