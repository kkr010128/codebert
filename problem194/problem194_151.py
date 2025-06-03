MOD = 10**9 + 7
INT_MAX = (1 << 63) - 1


if __name__ == "__main__":
    # test_case_num = int(input())

    # for _ in range(test_case_num):
    m, n = map(int, input().split())
    grid = [input().strip() for _ in range(m)]

    dp = [float('inf')] * n
    for i, row in enumerate(grid):
        for j, val in enumerate(row):
            if i == 0 and j == 0:
                dp[j] = grid[0][0] == '#'
            else:
                temp = INT_MAX
                if i > 0:
                    temp = min(dp[j] + (val == '#' != grid[i-1][j]), temp)
                if j > 0:
                    temp = min(dp[j-1] + (val == '#' != grid[i][j-1]), temp)
                dp[j] = temp
        # print(dp)

    print(dp[-1])
