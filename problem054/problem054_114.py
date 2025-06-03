from collections import OrderedDict

cards = OrderedDict()
cards['S'] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
cards['H'] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
cards['C'] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
cards['D'] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

cardnow = int(input())
for j in range(cardnow):
    s,n = [i for i in input().split()]
    n = int(n)
    cards[s].remove(n)

for k,v in cards.items():
    for vv in v:
        print('{} {}'.format(k,vv))