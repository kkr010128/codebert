N, K = [int(i) for i in input().split(" ")]

N = N % K
if (K - N) < N:
  N = K - N
print(N)