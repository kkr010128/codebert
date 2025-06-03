while True:
    text = input()
    if text == '-':
        break

    count = int(input())
    for c in range(count):
        index = int(input())
        text = text[index:] + text[:index]

    print(text)