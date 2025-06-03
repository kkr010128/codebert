card_dk = int(input())
block = ['S','H','C','D']
no = [1,2,3,4,5,6,7,8,9,10,11,12,13]
card_st =[]
not_card =[]
for i in range(card_dk):    
    card = input().split()
    card[1] = int(card[1])
    card_st.append(card)


for ch_block in block:
    for ch_no in no:
        flag = 0
        for card in card_st:
            if card == [ch_block,ch_no]:
                flag = 1
        if flag == 0:
            card = [ch_block,ch_no]
            not_card.append(card)

for fud_card in not_card:
    print('{} {}'.format(fud_card[0],fud_card[1]))
