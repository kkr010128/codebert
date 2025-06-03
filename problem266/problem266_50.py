def solve():
    X = int(input())
    p = int(X / 100)
    q = X % 100
    if 0 <= q <= 5 * p:
        print(1)
    else:
        print(0)

if __name__ == "__main__":
    solve()