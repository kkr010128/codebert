N = int(input())

def solve(x1, y1, x2, y2, n):
    if n == 0:
        return print(x1, y1)
    else:
        solve(x1, y1, (2 * x1 + x2) / 3, (2 * y1 + y2) / 3, n - 1)
        solve((2 * x1 + x2) / 3, (2 * y1 + y2) / 3, (x1 + x2) / 2 + (y1 - y2) * (3 ** (1 / 2)) / 6, (y1 + y2) / 2 + (x2 - x1) * (3 ** (1 / 2)) / 6, n - 1)
        solve((x1 + x2) / 2 + (y1 - y2) * (3 ** (1 / 2)) / 6, (y1 + y2) / 2 + (x2 - x1) * (3 ** (1 / 2)) / 6, (x1 + 2 * x2) / 3, (y1 + 2 * y2) / 3, n - 1)
        solve((x1 + 2 * x2) / 3, (y1 + 2 * y2) / 3, x2, y2, n - 1)

solve(0, 0, 100, 0, N)
print(100, 0)

