K, N = map(int, input().split())
A = list(map(int, input().split()))
distance = [0] * N
for i in range(N):
    if not i == N-1:
        distance[i] =  A[i+1] - A[i]
    else:
        distance[N-1] = A[0] + (K - A[N-1])
distance.sort()
distance.pop()
print(sum(distance))
