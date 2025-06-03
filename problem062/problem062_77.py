while True:
    text = input()
    if text == '0':
        break

    total = 0
    for a in range(len(text)):
        total += int(text[a])

    print(total)