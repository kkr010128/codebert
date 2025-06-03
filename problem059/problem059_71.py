#!usr/bin/env python3

import sys


def main():
    r, c = [int(row_col) for row_col in sys.stdin.readline().split()]
    sheet = [
                [int(row_num) for row_num in sys.stdin.readline().split()]
                for row in range(r)
            ]

    sheet.append([0 for col in range(c)])

    for row in range(len(sheet)-1):
        for col in range(len(sheet[0])):
            sheet[-1][col] += sheet[row][col]

    for row in sheet:
        row.append(sum(row))
        print(*row)


if __name__ == '__main__':
    main()