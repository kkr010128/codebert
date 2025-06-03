X = int(input())

found = False
for a in range(-200, 200):
    if found: break;
    for b in range(-200, 200):
        if a ** 5 - b ** 5 == X:
            print(a, b)
            found = True
            break
