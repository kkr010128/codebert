n = input()
taro = 0
hanako = 0

for i in xrange(n):
    t_card, h_card = raw_input().split(" ")

    if t_card < h_card:
        hanako += 3
    elif t_card > h_card:
        taro += 3
    elif t_card == h_card:
        taro += 1
        hanako += 1

print taro, hanako