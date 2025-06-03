n = int(input())
cards = [[0 for i in range(13)] for j in range(4)]

for i in range(n):
    Input = input().split()
    if Input[0] == "S":
        cards[0][int(Input[1])-1]= 1
    if Input[0] == "H":
        cards[1][int(Input[1]) - 1] = 1
    if Input[0] == "C":
        cards[2][int(Input[1]) - 1] = 1
    if Input[0] == "D":
        cards[3][int(Input[1]) - 1] = 1

for i in range(4):
    for j in range(13):
        if cards[i][j] == 0:
            if i == 0:
                print("S",j+1)
            if i == 1:
                print("H",j+1)
            if i == 2:
                print("C", j + 1)
            if i == 3:
                print("D", j + 1)