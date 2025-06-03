N , M = map(int,input().split())
ans = 0
ans += N * (N - 1) // 2
ans += M * (M - 1) // 2

print( ans )