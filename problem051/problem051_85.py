# coding: utf-8
board = ['#', '.']
while True:
    h, w = map(int, input().split())
    if h == 0 and w == 0:
        exit()
    for row in range(h):
        for column in range(w):
            print(board[(row + column) % 2], end='')
        print()
    print()

