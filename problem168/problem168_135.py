N, M = map(int, input().split())
A = map(int, input().split())
A_sum = sum(A)

if (N - A_sum) >= 0:
    print(N - A_sum)
else:
    print(-1)