def resolve():
    H = int(input())
    ans = 1
    while H > 0:
        ans *= 2
        H //= 2
    print(ans - 1)


resolve()
