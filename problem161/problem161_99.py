A, B, N = map(int, input().split())
m = B - 1 if N >= B else N
print(A * m // B)
