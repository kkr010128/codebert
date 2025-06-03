N = int(input())

ans = 0
for x in range(1, N + 1):
    n = N // x
    #ans += n * (2 * x + (n - 1) * x) // 2
    ans += n * ( x + n * x) // 2

print(ans)
