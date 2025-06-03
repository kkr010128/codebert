suit = {"S": 0, "H": 1, "C": 2, "D": 3}
suit_keys = list(suit.keys())
deck = [[suit_keys[i] + " " + str(j + 1) for j in range(13)] for i in range(4)]
for _ in range(int(input())):
    card = input().split()
    deck[suit[card[0]]][int(card[1]) - 1] = ""
for i in range(4):
    for j in range(13):
        if deck[i][j] != "":
            print(deck[i][j])

