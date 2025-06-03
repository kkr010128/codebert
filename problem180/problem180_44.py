N, K = map(int, input().split(' '))
rst = 0
rst = min(N % K, abs(N % K - K))
print(rst)