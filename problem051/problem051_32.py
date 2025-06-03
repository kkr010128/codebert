dataset = []

while True:
    h, w = map(int, input().split())
    if (h >= 1 and h <= 300) and (w >= 1 and w <= 300):
        listed = []
        listed.append(h)
        listed.append(w)
        dataset.append(listed)
    elif h != 0 and w != 0:
        break
    else:
        break

for listed in dataset:
    h = listed[0]
    w = listed[1]

    for i in range(h):
        if i % 2 == 0:
            for j in range(w):
                if j % 2 == 0:
                    print("#", end="")
                elif j % 2 == 1:
                    print(".", end="")
            print()
        elif i % 2 == 1:
            for j in range(w):
                if j % 2 == 0:
                    print(".", end="")
                elif j % 2 == 1:
                    print("#", end="")
            print()
    print()