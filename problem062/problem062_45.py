while True:

    x = input()

    if x == '0':
        break

    length = len(x)
    tot = 0

    for i in range(length):
        tot += int(x[i:i + 1])
    print(tot)
