K,N = map(int,input().split())
A = list(map(int,input().split()))
min_distance = 10000000
distance = 0

for i in range(N):
  if i == 0:
    distance = A[N-1] - A[0]
  elif i == N-1:
    distance = (K-A[i])+A[i-1]
  else:
    distance = (K-A[i+1])+A[i]
  if distance < min_distance:
    min_distance = distance
print(min_distance)