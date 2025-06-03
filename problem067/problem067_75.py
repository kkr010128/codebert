t = 0
h = 0

for i in range(int(input())):
    cards = input().split()
    if cards[0] > cards[1]:
        t += 3
    elif cards[0] == cards[1]:
        t += 1
        h += 1
    else:
        h += 3
        
print(str(t) + " " + str(h))