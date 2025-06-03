while True:
    data = input()
    if data == '0':
        break
    sum = 0
    for c in data:
        sum += int(c)
    print(sum)