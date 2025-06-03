def main():
    a_lst = [list(map(int, input().split())) for _ in range(3)]
    n = int(input())
    b_lst = [int(input()) for _ in range(n)]
    appear = [[False for _ in range(3)] for _ in range(3)]
    is_bingo = False

    for b in b_lst:
        for r in range(3):
            for c in range(3):
                if a_lst[r][c] == b:
                    appear[r][c] = True

    for r in range(3):
        if appear[r][0] == True and appear[r][1] == True and appear[r][2] == True:
            is_bingo = True

    for c in range(3):
        if appear[0][c] == True and appear[1][c] == True and appear[2][c] == True:
            is_bingo = True

    if appear[0][0] == True and appear[1][1] == True and appear[2][2] == True:
        is_bingo = True

    if appear[0][2] == True and appear[1][1] == True and appear[2][0] == True:
        is_bingo = True

    if is_bingo:
        ans = "Yes"
    else:
        ans = "No"

    print(ans)


if __name__ == "__main__":
    main()
