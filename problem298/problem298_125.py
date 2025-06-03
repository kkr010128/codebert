N,K = map(int,input().split())
height = list(map(int,input().split()))
chibi = [1] * N
for i in range (N):
  if height[i] >= K:
    chibi[i] = 0
print(N-sum(chibi))