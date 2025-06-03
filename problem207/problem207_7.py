import sys
from itertools import product


def main():
    input = sys.stdin.buffer.readline
    card = [[0] * 3 for _ in range(3)]
    for i in range(3):
        line = list(map(int, input().split()))
        card[i] = line
    mark = [[0] * 3 for _ in range(3)]
    n = int(input())
    for _ in range(n):
        b = int(input())
        for i, j in product(range(3), repeat=2):
            if card[i][j] == b:
                mark[i][j] = 1
                break

    for i in range(3):
        s = 0
        for j in range(3):
            s += mark[i][j]
        if s == 3:
            print("Yes")
            sys.exit()

    for j in range(3):
        s = 0
        for i in range(3):
            s += mark[i][j]
        if s == 3:
            print("Yes")
            sys.exit()

    s = 0
    for i in range(3):
        s += mark[i][i]
    if s == 3:
        print("Yes")
        sys.exit()

    s = 0
    for i in range(3):
        s += mark[i][2 - i]
    if s == 3:
        print("Yes")
        sys.exit()

    print("No")


if __name__ == "__main__":
    main()
