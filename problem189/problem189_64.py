N,M = map(int, input().split())
S = N+M
ans = S*(S-1) / 2 - N * M
print(int(ans))
