deck = {"S":[0]*13, "H":[0]*13, "C":[0]*13, "D":[0]*13} 

n = input()

for i in range(0, n):
    suit, num = raw_input().split(" ")
    deck[suit][int(num)-1] = 1

for i in ["S", "H", "C", "D"]:
    for j in range(0, 13):
        if (deck[i][j] == 0):
            print("%s %d" % (i, j+1))