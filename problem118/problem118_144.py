def solve(n):
    ans = 0
    for i in range(1, n+1):
        m = n // i
        ans += m * (m+1) * i // 2
    return ans

n = int(input())
print(solve(n))