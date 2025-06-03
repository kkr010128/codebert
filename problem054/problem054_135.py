mark = ["S","H","C","D"]
numbers = ["1","2","3","4","5","6","7","8","9","10","11","12","13"]

cardlist = {}

for m in mark:
    for n in numbers:
        key = m + " " + n
        cardlist[key] = 0


n = int(input())

for _ in range(n):
    card = input()
    cardlist[card] = 1


for card in cardlist:
    if cardlist[card] == 0:
        print(card)
