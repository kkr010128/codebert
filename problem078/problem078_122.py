N = int(input())
ans = pow(10, N, mod=1000000007) - pow(9, N, mod=1000000007) - pow(9, N, mod=1000000007) + pow(8, N, mod=1000000007)
ans %= 1000000007
print(ans)
