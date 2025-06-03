N,K = map(int,input().split())
scores = list(map(int,input().split()))
for i in range(N-K):
  #print(scores[K-K+i:K+i+1],scores[K-K + i],scores[K+i])
  if scores[K-K + i ] >= scores[K+i]:
    print("No")
  else:
    print("Yes")