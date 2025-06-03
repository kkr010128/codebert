n = int(input())
full_set=set([x for x in range(1,14)])
cards={"S":[],"H":[],"C":[],"D":[]}
for i in range(n):
    suit,num = input().split()
    cards[suit].append(int(num))
for suit in ["S","H","C","D"]:
    suit_set = set(cards[suit])
    for num in sorted(list(full_set - suit_set)): print(suit,num)