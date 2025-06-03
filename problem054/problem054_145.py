def create_card():
    return [str(i) for i in range(1,14)]
Card = {
        'S':create_card(),
        'H':create_card(),
        "C":create_card(),
        "D":create_card(),
        }
for i in range(int(input())):
    in_str = input().split()
    Card[in_str[0]].remove(in_str[1])

for s in ['S','H','C','D']:
    while(Card[s]):
        print(s,Card[s].pop(0))