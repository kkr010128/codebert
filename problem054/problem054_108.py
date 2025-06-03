N=int(input())
s=[input() for i in range(N)]
lost_list=[]
taro_card=[]
card_list=[]
for i in s:
    taro_card.append(i.split())
for i in range(1,14):
    card_list.append(["S",str(i)])
for i in range(1,14):
    card_list.append(["H",str(i)])
for i in range(1,14):    
    card_list.append(["C",str(i)])
for i in range(1,14):    
    card_list.append(["D",str(i)])
for i in card_list:
    if i not in taro_card:
        lost_list.append(i)
for i in lost_list:
    print(i[0]+" "+i[1])
