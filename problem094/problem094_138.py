#!/usr/bin/env python3


def next_line():
    return input()


def next_int():
    return int(input())


def next_int_array_one_line():
    return list(map(int, input().split()))


def next_int_array_multi_lines(size):
    return [int(input()) for _ in range(size)]


def next_str_array(size):
    return [input() for _ in range(size)]


def main():
    r, c, k = map(int, input().split())
    dp = [[[0] * (c+1) for i in range(r+1)] for i in range(4)]
    v = [[0] * (c+1) for i in range(r+1)]
    for i in range(k):
        row, col, val = map(int, input().split())
        v[row][col] = val

    for row in range(1, r + 1):
        for col in range(1, c + 1):
            for num in range(0, 4):
                if num == 0:
                    dp[num][row][col] = dp[3][row-1][col]  # simple down
                else:
                    
                    dp[num][row][col] = max(dp[num-1][row][col],  # str
                                            dp[num][row][col-1],  # right x
                                            dp[3][row-1][col] + \
                                            v[row][col],  # down o
                                            dp[num-1][row][col-1] + \
                                            v[row][col],  # right o
                                            )
    print(dp[3][r][c])


if __name__ == '__main__':
    main()
