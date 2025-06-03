k, n = map(int, input().split())
A = list(map(int, input().split()))

farthest = (k-A[-1])+A[0]
for i in range(len(A)-1):
    farthest = max(farthest, A[i+1]-A[i])
print(k-farthest)
