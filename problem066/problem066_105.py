results = []
while True:
    cards = input()
    if cards == '-':
        break
    
    for i in range(int(input())):
        n = int(input())
        cards = cards[n:] + cards[:n]
    results.append(cards)
    
for line in results:
    print(line)