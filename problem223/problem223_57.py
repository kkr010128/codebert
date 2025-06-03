N, K = map(int, input().split())
P = list(map(int, input().split()))

res = 0

P2 = []
for i in P:
  P2.append(0.5 * (i + 1))
num = 0
for i in range(K):
  num += P2[i]
res = num
for i in range(1,N-K+1):
  temp = num + P2[i+K-1] - P2[i-1]
  if temp > res:
    res = temp
  num = temp
  
print(res)