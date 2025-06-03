def solve(n):
    if n <= 1:
        print(1)
        return

    a, b = 1, 1
    for _ in range(2, n + 1):
        c = a + b
        b = a
        a = c
    print(c)

if __name__ == "__main__":
    n = int(input())
    solve(n)
