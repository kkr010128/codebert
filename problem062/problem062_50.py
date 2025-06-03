while True:
    total = 0
    x = input()
    if x == "0": break
    for c in x:
        total += int(c)
    print(total)

