N, M = map(int, input().split())
A = list(map(int, input().split()))

w = sum(A)
ans = N - w

if ans >= 0:
    print(ans)
else:
    print(-1)