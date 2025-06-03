N, K, S = map(int, input().split())


if S < 10**9:
    T = S + 1
else:
    T = S - 1
ans = [S]*K + [T]*(N-K)
print(*ans)