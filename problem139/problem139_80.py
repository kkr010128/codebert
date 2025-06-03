H1, M1, H2, M2, K = map(int, input().split())

s = 60 * H1 + M1
e = 60 * H2 + M2
ans = max(0, e - s - K)
print(ans)
