N, M = map(int, input().split())
A = list(map(int, input().split()))

k = sum(A) / (4*M)
print('Yes' if [a >= k for a in A].count(True) >= M else 'No')