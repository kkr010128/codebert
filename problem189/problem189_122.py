N,M = map(int, input().split())
ans1 = 0
ans2 = 0

ans1 = N*(N-1)/2
ans2 = M*(M-1)/2

print(int(ans1 + ans2))
