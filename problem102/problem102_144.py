n, k = map(int, input().split())
A = [*map(int, input().split())]
for i in range(n-k): print('Yes' if A[i] < A[i+k] else 'No')
