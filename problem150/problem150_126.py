N, K = map(int, input().split())

A = [[0 for _ in range(N+1)] for _ in range(100)]
A[0] = [0] + list(map(int, input().split()))

for l in range(1,100):
  #print(A[0])
  for j in range(1, N+1):
    #print(l,j)
    #print(l-1,A[l-1][j])
    A[l][j] = A[l-1][A[l-1][j]] #2^(l-1)1回テレポート後、さらに^(l-1)1回テレポート
  if 2 ** l > K:
    break

k = K
ans = 1
keta = 0
while k > 0:
  if k & 1:
    ans = A[keta][ans]
  k = k >> 1
  keta += 1

print(ans)
        
        
        

