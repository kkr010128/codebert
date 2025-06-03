N = int(input())
CardList = [0 for i in range(53)]
for i in range(1, N + 1):
    Mark, Rank = map(str, input().split())
    if Mark == 'S':
        CardList[int(Rank) ] = 1
    elif Mark == 'H':
        CardList[int(Rank) + 13] = 1
    elif Mark == 'C':
        CardList[int(Rank) + 26] = 1
    else:
        CardList[int(Rank) + 39] = 1
for j in range(1, 53):
    if CardList[j] == 0:
        if 1 <= j <14:
            print('S', j)
        elif 14 <= j < 27:
            print('H', j - 13)
        elif 27 <= j <40:
            print('C', j - 26)
        else:
            print('D', j - 39)

