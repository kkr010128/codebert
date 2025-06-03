K, N = map(int, input().split())
A = list(map(int, input().split()))

dists = []
for i in range(N):
  if i==N-1:
    dists.append(K-A[N-1]+A[0])
                 
  else:
    dists.append(A[i+1]-A[i])
    
print(K-max(dists))