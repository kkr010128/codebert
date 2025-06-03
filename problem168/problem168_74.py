N, M = map(int, input().split())
A = sum(map(int, input().split()))
if N-A >= 0:
    print(N-A)
else:
    print(-1)
