N, K = map(int, input().split())
A = N % K
B = K - A
print(min(A, B))