N, K = map(int, input().split())
Max = [0]
Min = [0]
for i in range(1, N+2):
  Max.append(N-i+1+Max[i-1])
  Min.append(i-1+Min[i-1])
A = [mx-mn+1 for mx,mn in zip(Max,Min)]
B =[0]
for i in range(N+1):
  B.append(B[i]+A[i+1])
print((B[N+1]-B[K-1])%(10**9+7))