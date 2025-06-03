h, m, H, M, K = map(int, input().split())
print(H * 60 + M - h * 60 - m - K)
