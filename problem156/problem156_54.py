X = int(input())

for a in range(-119, 120):
    for b in range(-119, 120):
        if X == a**5 - b**5:
            la = a
            lb = b
print(la, lb)
