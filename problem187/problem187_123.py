n, x, y = map(int, input().split())
x -= 1
y -= 1

def main():
    ans = {}
    for i in range(1, n):
        ans[i] = 0

    for i in range(0, n - 1):
        for j in range(i + 1, n):
            ans[solve(i, j)] += 1

    for k in range(1, n):
        print(ans[k])

def solve(i, j):
    """
    最短距離を計算する
    O(1)
    """

    dist = min(abs(i - j), abs(x - i) + abs(y - j) + 1, abs(y  -i) + abs(x - j) + 1)

    return dist

if __name__ == '__main__':
    main()