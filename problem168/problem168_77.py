N, M = [int(_) for _ in input().split()]
A = [int(_) for _ in input().split()]
print(max(N - sum(A), -1))
