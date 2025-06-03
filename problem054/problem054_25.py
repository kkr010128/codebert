n = input()
mark = ['S', 'H', 'C', 'D']
cards = ["{} {}".format(mark[i], j+1) for i in range(4) for j in range(13)]
for i in range(n):
    cards.remove(raw_input())
while len(cards) != 0:
    print cards.pop(0)