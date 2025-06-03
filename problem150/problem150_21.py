N, K = map(int, input().split())
A = list(map(int, input().split()))
visited = [-1 for _ in range(N)]
visited[0] = 0
k = 0
k = A[k] - 1
count = 0
while visited[k] == -1:
  count += 1
  visited[k] = count
  k = A[k]-1
 
roop = count - visited[k] + 1
beforeroop = visited[k]
 
if K < beforeroop:
  k = 0
  for _ in range(K):
    k = A[k] - 1
  print(k+1)
else:
  K = K - beforeroop
  K = K % roop
 
  for _ in range(K):
    k = A[k]-1
  print(k+1)