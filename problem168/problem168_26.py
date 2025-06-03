N, M = map(int, input().split())
A = list(map(int, input().split()))

days = N - sum(A)
print(days) if days >= 0 else print('-1')