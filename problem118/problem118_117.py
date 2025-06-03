def solve():
    ret = 0
    for k in range(1, N + 1):
        y = N // k
        ret += k * y * (y + 1) // 2
    print(ret)

if __name__ == "__main__":
    N = int(input())
    solve()