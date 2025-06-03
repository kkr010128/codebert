K, N = map(int, input().split())
A = list(map(int, input().split()))
a_old = A[0]
ma = A[0] + K - A[-1]
for a in A[1:]:
    ma = max(ma, a - a_old)
    a_old = a
print(K-ma)
