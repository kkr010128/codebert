#!/usr/bin/env python3
def main():
    A = []
    for i in range(3):
        A.append([int(x) for x in input().split()])
    N = int(input())
    bingo = [[False] * 3 for _ in range(3)]
    for n in range(N):
        B = int(input())
        for i in range(3):
            if B in A[i]:
                bingo[i][A[i].index(B)] = True
    for i in range(3):
        if bingo[i][0] == bingo[i][1] == bingo[i][2] is True:
            print('Yes')
            return
        if bingo[0][i] == bingo[1][i] == bingo[2][i] is True:
            print('Yes')
            return
    if bingo[0][0] == bingo[1][1] == bingo[2][2] is True:
        print('Yes')
        return
    if bingo[0][2] == bingo[1][1] == bingo[2][0] is True:
        print('Yes')
        return
    print('No')


if __name__ == '__main__':
    main()
