def solve():
    MOD = 10**9 + 7

    N = int(input())
    As = list(map(int, input().split()))

    ans = 0
    for d in range(60):
        mask = 1<<d
        num1 = len([1 for A in As if A & mask])
        ans += num1 * (N-num1) * mask
        ans %= MOD

    print(ans)


solve()
