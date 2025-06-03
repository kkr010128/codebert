cards = []
mark = ["S","H","C","D"]
for i in range(4):
    mk = mark[i]
    for j in range(1,14):
        cards.append("{} {}".format(mk,j))
n = int(input())
for _ in range(n):
    card = input()
    cards.remove(card)
for i in cards:
    print(i)