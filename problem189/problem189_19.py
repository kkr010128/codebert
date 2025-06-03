N, M = [int(x) for x in input().split()]

result = N * (N - 1) // 2 + M * (M - 1) // 2
print(result)
