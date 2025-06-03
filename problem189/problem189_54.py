def solve():
    N,M = [int(i) for i in input().split()]
    ans = 0
    if N > 1:
        ans += N * (N-1) // 2
    if M > 1:
        ans += M * (M-1) // 2
    print(ans)

if __name__ == "__main__":
    solve()