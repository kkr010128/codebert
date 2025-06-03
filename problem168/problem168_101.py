N, M = map(int, input().split())
A = list(map(int, input().split()))
A1 = sum(A)

if N - A1 >= 0:
    print(N - A1)
else:
    print("-1")