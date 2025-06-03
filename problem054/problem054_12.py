n = int(input())
cards = ["{0} {1}".format(design, num) for design in ["S", "H", "C", "D"] for num in range(1, 14)]

for _ in range(n):
    cards.remove(input())
    
for card in cards:
    print(card)