import sys
from collections import deque
input = sys.stdin.readline

def main():
    h, w, k = map(int, input().split())
    board = [input().strip() for i in range(h)]

    group = [[0 for i in range(w)] for j in range(h)]

    state = 0   # 0:not found, 1:one strawberry
    num = 1
    stock = 1
    pre = -1
    for i in range(h):
        if "#" not in board[i]:
            stock += 1
            continue
        for j in range(w):
            if board[i][j] == "#":
                if state == 0:
                    state = 1
                else:
                    num += 1
                group[i][j] = num
            else:
                group[i][j] = num
        for k in range(stock):
            for j in range(w):
                print(group[i][j], end=" ")
            print()
        num += 1
        state = 0
        stock = 1
        pre = i
    
    for k in range(h-pre-1):
        for j in range(w):
            print(group[pre][j], end=" ")
        print()


if __name__ == "__main__":
    main()