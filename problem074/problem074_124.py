N,K = map(int,input().split())
L = []
for _ in range(K):
  l,r = map(int,input().split())
  L.append((l,r))
DP = [0] * N
DP[0] = 1
con = [0] * (N + 1)
con[1] = 1
for i in range(1 , N):
  s = 0
  for l,r in L:
    s += con[max(0 , i - l + 1)] - con[max(0 , i - r)]
  DP[i] = s
  con[i + 1] = (con[i] + DP[i]) % 998244353
  
print(DP[N - 1] % 998244353)

      
      
      
