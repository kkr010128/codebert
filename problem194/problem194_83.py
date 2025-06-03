def main():
    height, width = map(int, input().split())
    grid = [list(input()) for _ in range(height)]
    dp = [[float("inf") for _ in range(width)] for _ in range(height)]
    if grid[0][0] == "#":
        dp[0][0] = 1
    else:
        dp[0][0] = 0
    delta = [[0, 1], [1, 0]]
    for i in range(height):
        for j in range(width):
            for dx, dy in delta:
                if i + dy >= height or j + dx >= width:
                    continue
                else:
                    add = 0
                    if grid[i][j] == "." and grid[i + dy][j + dx] == "#":
                        add = 1
                    dp[i + dy][j + dx] = min(dp[i + dy][j + dx], dp[i][j] + add)
    print(dp[-1][-1])


if __name__ == '__main__':
    main()

