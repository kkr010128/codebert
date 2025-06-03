def main():
    bingo = []
    for ss in range(3):
        s = list(map(int,input().strip().split()))
        bingo.append(s)
    
    n = int(input())
    nl = []
    for nn in range(n):
        nl.append(int(input()))
    
    for i in range(3):
        for j in range(3):
            for n in nl:
                if bingo[i][j] == n:
                    bingo[i][j] = -1
    
    for i in range(3):
        if bingo[0][i] == bingo[1][i] == bingo[2][i] == -1:
            print("Yes")
            return
        if bingo[i][0] == bingo[i][1] == bingo[i][2] == -1:
            print("Yes")
            return
    
    if bingo[0][0] == bingo[1][1] == bingo[2][2] == -1:
        print("Yes")
        return
    if bingo[0][2] == bingo[1][1] == bingo[2][0] == -1:
        print("Yes")
        return
    
    print("No")
    return

    
main()
