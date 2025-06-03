A, B, C, K = [int(_) for _ in input().split()]
print(K if K <= A else A if K <= A + B else A - (K - A - B))
