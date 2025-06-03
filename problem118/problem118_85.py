def solve():
    N = int(input())
    ans = 0
    for i in range(1, N+1):
        d = N//i
        ans += i * d * (d + 1) / 2
    print(int(ans))

solve()