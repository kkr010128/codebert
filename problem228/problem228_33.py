def solve():
    H = int(input())
    cnt = 0
    ans = 0
    while H > 0:
        ans += 2**cnt
        if H == 1:
            break
        H = H // 2
        cnt += 1
    print(ans)


if __name__ == "__main__":
    solve()