N, M = map(int, input().split())
A = list(map(int, input().split()))

day = N - sum(A)

if N - sum(A) >= 0:
    print(day)

elif N - sum(A) < 0:
    print(-1)
