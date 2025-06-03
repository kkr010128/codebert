n = int(raw_input())
s = ["S"]
h = ["H"]
c = ["C"]
d = ["D"]
card_list = [s,h,c,d]

for i in range(n):
    card = raw_input().split()
    for v in card_list:
        if v[0] == card[0]:
            v.append(int(card[1]))
# print card_list

for i in card_list:
    for j in range(1, 14):
        if not j in i:
            print "%s %d" % (i[0], j)