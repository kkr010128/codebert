def solve():
    n, k = map(int, input().split())
    h = list(map(int, input().split()))
    ans = 0
    for i in h:
        if i >= k:
            ans += 1
    print(ans)
    return 0

if __name__ == "__main__":
    solve()