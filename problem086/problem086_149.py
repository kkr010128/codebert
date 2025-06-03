N, X, T = map(int, input().split())

ans = T * (N // X)
ans = ans if (N % X) is 0 else ans + T

print(ans)
