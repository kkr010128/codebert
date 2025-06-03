import sys
sys.setrecursionlimit(100000)


def input():
    return sys.stdin.readline().strip()


def input_int():
    return int(input())


def input_int_list():
    return [int(i) for i in input().split()]


def main():
    h, w, k = input_int_list()
    num = 0
    grid = []
    for _ in range(h):
        grid.append(list(input()))

    # 分割統治法
    def solver(x_b, y_b, x_e, y_e):  # x_end,y_endは包含/排他範囲
        # いちごの数を数える
        cnt = 0
        first = None
        second = None
        for i in range(x_b, x_e):
            for j in range(y_b, y_e):
                if grid[i][j] == "#":
                    cnt += 1
                    if not first:
                        first = [i, j]
                    elif not second:
                        second = [i, j]
        if cnt == 1:
            nonlocal num
            num += 1
            for i in range(x_b, x_e):
                for j in range(y_b, y_e):
                    grid[i][j] = num
            return
        # いちごが少なくとも1つ含まれるように分割する
        if cnt > 1:
            if first[0] != second[0]:
                x_edge = max(first[0], second[0])
                solver(x_b, y_b, x_edge, y_e)
                solver(x_edge, y_b, x_e, y_e)
            elif first[1] != second[1]:
                y_edge = max(first[1], second[1])
                solver(x_b, y_b, x_e, y_edge)
                solver(x_b, y_edge, x_e, y_e)

    solver(0, 0, h, w)
    for line in grid:
        print(*line)

    return


if __name__ == "__main__":
    main()
